<template>
  <div class="simulationscontainer">
    <div class="extremecontainer">
      <b-container fluid class="description">
        <h1 class="text-secondary">{{ $t("simulations") }}</h1>
        <h3 class="text-secondary">{{ $t("simulationDescription") }}</h3>
      </b-container>
    </div>
    <div class="middlecontainer">
      <b-spinner label="Loading..." v-if="loading"></b-spinner>

      <b-container fluid class="calculator bg-secondary text-primary">
        <b-row>
          <b-col
            ><h2>{{ $t("calculate") }}</h2></b-col
          >
          <b-col
            ><v-select
              class="style-chooser"
              @input="updateType"
              :options="calculationOptions"
              v-model="selectedSim"
            ></v-select
          ></b-col>
        </b-row>

        <b-row v-for="input in inputs" :key="input.name">
          <b-col
            ><h5>{{ $t(input.name) }}</h5></b-col
          >
          <b-col
            ><b-form-input
              v-model="input.value"
              :readonly="selected === input.name"
              :formatter="input.formatter"
              @input="update"
            ></b-form-input
          ></b-col>
        </b-row>
        <b-container fluid class="buttons">
          <b-row cols="12">
            <b-col cols="5">
              <b-form-input v-model="simName" placeholder="Nome"></b-form-input>
            </b-col>
            <b-col cols="3">
              <b-button
                class="text-primary"
                pill
                variant="success"
                @click="save"
              >
                {{ $t("save") }}
              </b-button>
            </b-col>
            <b-col cols="3">
              <b-button
                class="text-primary"
                pill
                variant="danger"
                @click="clean"
              >
                {{ $t("clear") }}
              </b-button>
            </b-col>
            <div v-if="incorrect">
              {{ $t("errorSimulation") }}
            </div>
          </b-row>
        </b-container>
      </b-container>

      <b-container fluid class="saved-simulations bg-secondary text-primary">
        <h2>{{ $t("savedSimulations") }}</h2>
        <b-table
          small
          fixed
          sticky-header="true"
          dark
          hover
          :items="simulations"
          :fields="fields"
        >
          <template #cell(actions)="row">
            <b-button
              variant="primary"
              size="sm"
              @click="selectRow(row.item, row.index, $event.target)"
              class="mr-1"
            >
              {{ $t("see") }}
            </b-button>
            <b-button
              variant="danger"
              size="sm"
              @click="remove(row.item, row.index, $event.target)"
              class="mr-1"
            >
              {{ $t("remove") }}
            </b-button>
          </template>
        </b-table>
      </b-container>
    </div>
    <div class="extremecontainer"></div>
  </div>
</template>

<style>
.style-chooser .vs__search::placeholder,
.style-chooser .vs__dropdown-toggle,
.style-chooser .vs__dropdown-menu {
  background: #fbfcfc;
  border: none;
  color: #6bbe0c;
  text-transform: lowercase;
  font-variant: small-caps;
}

.style-chooser .vs__clear,
.style-chooser .vs__open-indicator {
  fill: #394066;
}
</style>

<style scoped>

.calculator {
  width: 40%;
  height: 100%;
  display: flex;
  flex-direction: column;
  border-radius: 20px;
  justify-content: space-evenly;
}

.saved-simulations {
  padding: 20px;
  width: 40%;
  height: 100%;
  border-radius: 20px;
}

.simulationscontainer {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100%;
  width: 100%;
}

.extremecontainer {
  width: 100%;
  height: 20%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.middlecontainer {
  width: 100%;
  height: 60%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
}
</style>


<script>
import i18n from "@/plugins/i18n";
import vSelect from "vue-select";
import axios from "axios";
import Client from "../repositories/Clients/AxiosClient";

export default {
  name: "Simulations",
  components: {
    vSelect,
  },
  data() {
    return {
      dialog: false,
      selected: null,
      selectedSim: null,
      incorrect: false,
      loading: false,
      simulations: [],
      fields: [
        {
          key: "name",
          sortable: true,
          label: this.$t("name"),
        },
        {
          key: "created_at",
          sortable: true,
          label: this.$t("created_at"),
        },
        {
          key: "actions",
          label: this.$t("actions"),
        },
      ],
      calculationOptions: [
        { label: this.$t("initial"), name: "initial" },
        { label: this.$t("monthly"), name: "monthly" },
        { label: this.$t("time"), name: "time" },
        { label: this.$t("final"), name: "final" },
      ],
      values: {
        initial: null,
        monthly: "0",
        time: null,
        interest: "6.00",
        final: null,
      },
      inputs: [
        {
          name: "initial",
          originalIndex: 0,
          formatter: this.currencyFormat,
          value: null,
        },
        {
          name: "monthly",
          originalIndex: 1,
          formatter: this.currencyFormat,
          value: null,
        },
        { name: "time", originalIndex: 2, value: null },
        {
          name: "interest",
          originalIndex: 3,
          formatter: this.percentageFormat,
          value: "6.00",
        },
        {
          name: "final",
          originalIndex: 4,
          formatter: this.currencyFormat,
          value: null,
        },
      ],
      simName: "",
    };
  },
  mounted() {
    let prevSim = localStorage.getItem("simValues");
    if (prevSim != null) {
      this.values = JSON.parse(prevSim);
      if (this.values != null)
        this.inputs.forEach((v, i, a) => (v.value = this.values[v.name]));
    }
    localStorage.removeItem("simValues");
    if (this.$store.getters.isLoggedIn) this.fetchSimulations();
    this.selectedSim = this.calculationOptions[3];
    this.selected = "final";
  },
  methods: {
    currencyFormat(value) {
      return this.toCurrency(this.toNumber(value) / 100);
    },
    percentageFormat(value) {
      return (this.toNumber(value) / 100).toLocaleString("pt-BR", {
        maximumFractionDigits: 2,
        minimumFractionDigits: 2,
      });
    },
    update() {
      this.inputs.forEach((v, i, a) => (this.values[v.name] = v.value));

      let initial =
        this.selected !== "A" ? this.fromText(this.values.initial) : null;
      let monthly =
        this.selected !== "B" ? this.fromText(this.values.monthly) : null;
      let interest =
        this.selected !== "D"
          ? this.fromText(this.values.interest) / 100
          : null;
      let finalValue =
        this.selected !== "E" ? this.fromText(this.values.final) : null;

      let monthlyInterest = Math.pow(1 + interest, 1 / 12);
      let ratio = monthlyInterest ** this.values.time;

      if (this.selected === "final") {
        if (
          this.values.initial == null ||
          this.values.interest == null ||
          this.values.monthly == null ||
          this.values.time == null
        )
          return;
        let final =
          initial * ratio + (monthly * (ratio - 1)) / (monthlyInterest - 1);
        this.values.final = this.toCurrency(final);
      } else if (this.selected === "initial") {
        if (
          this.values.final == null ||
          this.values.interest == null ||
          this.values.monthly == null ||
          this.values.time == null
        )
          return;
        let init =
          (finalValue - (monthly * (ratio - 1)) / (monthlyInterest - 1)) /
          ratio;
        this.values.initial = this.toCurrency(init);
      } else if (this.selected === "monthly") {
        if (
          this.values.final == null ||
          this.values.interest == null ||
          this.values.initial == null ||
          this.values.time == null
        )
          return;
        let monthly =
          ((finalValue - initial * ratio) * (monthlyInterest - 1)) /
          (ratio - 1);
        this.values.monthly = this.toCurrency(monthly);
      } else if (this.selected === "time") {
        if (
          this.values.final == null ||
          this.values.interest == null ||
          this.values.initial == null ||
          this.values.monthly == null
        )
          return;
        let aux = monthly / (monthlyInterest - 1);
        let x = (finalValue + aux) / (initial + aux);
        let time = Math.log(x) / Math.log(monthlyInterest);
        this.values.time = Math.ceil(time);
      }
      this.inputs.forEach((v, i, a) => (v.value = this.values[v.name]));
    },
    toNumber(n) {
      return Number(n.replace(/[^0-9]+/g, ""));
    },
    toCurrency(n) {
      let currency = i18n.locale === "pt-br" ? "BRL" : "USD";
      return Number(n).toLocaleString("pt-BR", {
        style: "currency",
        currency: currency,
      });
    },
    fromText(n) {
      if (n == null) return null;
      return this.toNumber(n) / 100;
    },
    updateType(v) {
      console.log(this.inputs);
      this.selected = v.name;
      let retIndex = this.inputs[4].originalIndex;
      let bkp = this.inputs[retIndex];
      this.inputs[retIndex] = this.inputs[4];
      this.inputs[4] = bkp;

      let res = this.inputs.find((x) => x.name === v.name);
      this.inputs[res.originalIndex] = this.inputs[4];
      this.inputs[4] = res;
    },
    save() {
      this.inputs.forEach((v, i, a) => (this.values[v.name] = v.value));

      if (!this.$store.getters.isLoggedIn) {
        localStorage.setItem("simValues", JSON.stringify(this.values));
        this.$router.push("login");
      } else {
        const token = this.$store.state.token;
        this.loading = true;
        let { data } = Client(token)
          .post("/api/simulations/", {
            initial_value: this.fromText(this.values.initial),
            monthly_contribution: this.fromText(this.values.monthly),
            interest_rate: this.fromText(this.values.interest),
            final_amount: this.fromText(this.values.final),
            time: this.values.time,
            name: this.simName,
          })
          .then((response) => {
            this.fetchSimulations();
          })
          .catch((error) => {
            console.log(error);
            this.incorrect = true;
          });
      }
    },
    async fetchSimulations() {
      this.loading = true;
      if (this.$store.getters.isLoggedIn) {
        const token = this.$store.state.token;
        await Client(token)
          .get("/api/simulations/", {})
          .then((response) => {
            this.simulations = response.data;
          })
          .catch((error) => {
            console.log(error);
            this.incorrect = true;
          })
          .finally(() => (this.loading = false));
      }
    },
    async remove(item, index, button) {
      const token = this.$store.state.token;
      this.loading = true;
      await Client(token)
        .delete("/api/simulations/" + item.id + "/")
        .then((response) => {
          this.fetchSimulations();
        })
        .catch((error) => {
          console.log(error);
          this.incorrect = true;
        });
    },
    selectRow(item) {
      this.values.initial = this.toCurrency(item.initial_value);
      this.values.monthly = this.toCurrency(item.monthly_contribution);
      this.values.interest = this.percentageFormat(item.interest_rate);
      this.values.time = item.time;
      this.values.final = this.toCurrency(item.final_amount);
      this.inputs.forEach((v, i, a) => (v.value = this.values[v.name]));
    },
    clean() {
      this.values.initial = null;
      this.values.monthly = null;
      this.values.interest = "6.00";
      this.values.time = null;
      this.values.final = null;
      this.inputs.forEach((v, i, a) => (v.value = this.values[v.name]));
    },
  },
};
</script>