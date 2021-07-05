<template>
  <div class="box-externa">
    <b-container fluid class="outcontainer">
      <b-container class="bv-example-row">
        <b-row>
          <b-col cols="1" align-v="center">
            <b-nav-item to="/wallets">
              <h2 align="left">
                <b-icon-arrow-left-circle style="color: #47545d"
                  >></b-icon-arrow-left-circle
                >
              </h2>
            </b-nav-item>
          </b-col>
          <b-col align-v="center">
            <b-container class="box-title">
              <h1 class="text-dark">{{ $t("wallets") }}</h1>
            </b-container>
          </b-col>
          <b-col cols="1" align-v="center">
            <b-spinner label="Loading..." v-if="loading"></b-spinner>
          </b-col>
        </b-row>
      </b-container>

      <b-container
        class="bv-example-row bv-example-row-flex-cols p-0"
        v-if="!unauth && !firstLoading"
      >
        <b-row cols="12">
          <b-col cols="6">
            <b-container class="centerBox bg-secondary">
              <h3 class="text-primary">{{ $t("opInsert") }}</h3>
              <div class="container-fluid">
                <b-row class="my-3" align-h="center">
                  <b-col sm="3" align="center">{{ $t("wDay") }} </b-col>
                  <b-col cols="9">
                    <b-form-datepicker
                      id="example-datepicker"
                      v-model="day"
                      size="sm"
                    ></b-form-datepicker
                  ></b-col>
                </b-row>
                <b-row class="my-3" align-h="start">
                  <b-col sm="3" align="center">{{ $t("wQuantity") }} </b-col>
                  <b-col cols="9">
                    <b-form-input
                      v-model="quantity"
                      type="number"
                    ></b-form-input>
                  </b-col>
                </b-row>
                <b-row class="my-3" align-h="start">
                  <b-col sm="3" align="center">{{ $t("wValue") }} </b-col>
                  <b-col cols="9">
                    <b-form-input
                      v-model="value"
                      type="text"
                      :formatter="currencyFormat"
                    ></b-form-input>
                  </b-col>
                </b-row>
                <b-row class="my-3" align-h="start">
                  <b-col sm="3" align="center">{{ $t("wSymbol") }} </b-col>
                  <b-col cols="9">
                    <v-select
                      class="style-chooser"
                      :options="companies"
                      v-model="symbol"
                      :reduce="(x) => x.symbol"
                      label="name"
                    ></v-select>
                  </b-col>
                </b-row>

                <b-row class="my-1" align-h="center">
                  <b-button-group class="right-chart-options" cols="8">
                    <b-button
                      v-for="(btn, idx) in marketOptions.buttons"
                      :key="idx"
                      :pressed.sync="btn.state"
                      variant="primary"
                      @click="market = btn.value"
                    >
                      <flag :iso="btn.flag" v-bind:squared="false" />&nbsp;{{
                        btn.caption
                      }}
                    </b-button>
                  </b-button-group>
                </b-row>

                <b-row class="my-1" align-h="center">
                  <b-form-group>
                    <b-form-radio-group
                      id="radio-group-1"
                      v-model="opType"
                      :options="operationTypes"
                      name="radio-options"
                      class="text-primary"
                    ></b-form-radio-group>
                  </b-form-group>
                </b-row>

                <b-row class="my-1" align-h="center">
                  <b-button
                    pill
                    @click="submit"
                    class="bg-success text-primary"
                  >
                    {{ $t("insert") }}
                  </b-button>
                </b-row>
              </div>
            </b-container>
          </b-col>

          <b-col cols="6">
            <b-container class="rightBox bg-secondary">
              <h3 class="text-primary">{{ $t("currentComposition") }}</h3>
              <div class="container-fluid">
                <b-table
                  sticky-header="true"
                  no-border-collapse
                  small
                  dark
                  hover
                  :items="consolidated"
                  :fields="fieldsConsolidated"
                >
                </b-table>
              </div>
              <div class="valorAtual bg-primary">
                <h3 class="text-secondary">
                  Valor atual da carteira:
                  {{ this.toCurrency(currentTotalValue) }}
                </h3>
              </div>
            </b-container>
          </b-col>
        </b-row>
      </b-container>
    </b-container>
    <b-container class="bv-example-row bv-example-row-flex-cols" v-if="unauth">
      <h1 class="text-secondary">{{ $t('unauth') }}</h1>
    </b-container>
    <b-container fluid class="ccontainer" v-if="!unauth && !firstLoading">
      <b-row class="mt-3" align-h="center">
        <b-col class="pl-4" cols="12">
          <b-container class="centerBox bg-secondary">
            <h3 class="text-primary">{{ $t("opHistory") }}</h3>
            <div class="container-fluid">
              <b-table
                sticky-header="200px"
                no-border-collapse
                small
                fixed
                dark
                hover
                :items="opHistory"
                :fields="fields"
              >
                <template #cell(actions)="row">
                  <b-button
                    pill
                    variant="danger"
                    size="sm"
                    @click="remove(row.item, row.index, $event.target)"
                    class="mr-1"
                  >
                    {{ $t("remove") }}
                  </b-button>
                </template>
              </b-table>
            </div>
          </b-container>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<style scoped>
.style-chooser .vs__search::placeholder,
.style-chooser .vs__dropdown-toggle,
.style-chooser .vs__dropdown-menu {
  background: #dfe5fb;
  border: none;
  color: #394066;
  text-transform: lowercase;
  font-variant: small-caps;
}

.style-chooser .vs__clear,
.style-chooser .vs__open-indicator {
  fill: #394066;
}
.box-externa {
  display: flex;
  flex-direction: column;
  justify-content: start;
  width: 100%;
  height: 100%;
}
.back-button {
  height: 50%;
  width: 100%;
}
.box-title {
  padding: 10px;
}
.valorAtual {
  padding: 10px;
  border-radius: 20px;
  width: 100%;
}
.centerBox {
  border-radius: 20px;
  padding: 10px;
}
.rightBox {
  display: flex;
  flex-direction: column;
  align-content: center;
  border-radius: 20px;
  padding: 10px;
}
.outcontainer {
  width: 100%;
  height: 65%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
}

.ccontainer {
  width: 100%;
  height: 35%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  margin-bottom: 10px;
}
</style>

<script>
import i18n from "@/plugins/i18n";
import Client from "../repositories/Clients/AxiosClient";
import bovespaCompanies from "../data/bovespa.json";
import nasdaqCompanies from "../data/nasdaq.json";
import vSelect from "vue-select";
const BOVESPA = "BOVESPA";
const NASDAQ = "NASDAQ";
export default {
  name: "Wallets",
  mounted() {
    this.id = this.$route.params.id;
    this.fetchStocks();
  },
  components: {
    vSelect,
  },
  data() {
    return {
      day: "",
      market: BOVESPA,
      opType: "Buy",
      quantity: 0,
      value: 0,
      companies: bovespaCompanies,
      unauth: false,
      loading: true,
      firstLoading: true,
      marketOptions: {
        buttons: [
          { caption: "BOVESPA", state: true, value: BOVESPA, flag: "br" },
          { caption: "NASDAQ", state: false, value: NASDAQ, flag: "us" },
        ],
      },
      id: 0,
      symbol: "",
      opHistory: [],
      currentTotalValue: 0,
      consolidated: [],
      operationTypes: ["Buy", "Sell"],
      fields: [
        {
          key: "value",
          sortable: true,
          label: this.$t("value"),
        },
        {
          key: "type",
          sortable: true,
          label: this.$t("type"),
        },
        {
          key: "symbol",
          sortable: true,
          label: this.$t("stock"),
        },
        {
          key: "quantity",
          sortable: true,
          label: this.$t("quantity"),
        },
        {
          key: "day",
          sortable: true,
          label: this.$t("day"),
        },
        { key: "actions", label: "" },
      ],
      fieldsConsolidated: [
        {
          key: "symbol",
          sortable: true,
          label: this.$t("actions"),
        },
        {
          key: "quantity",
          sortable: true,
          label: this.$t("quantity"),
        },
        {
          key: "avg_value",
          sortable: true,
          label: this.$t("buyAvgValue"),
        },
        {
          key: "current_unit",
          sortable: true,
          label: this.$t("currentUnitValue"),
        },
        {
          key: "current_total",
          sortable: true,
          label: this.$t("currentTotalValue"),
        },
      ],
    };
  },
  methods: {
    currencyFormat(value) {
      return this.toCurrency(this.toNumber(value) / 100);
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
    submit() {
      const token = this.$store.state.token;
      let parsedSymbol =
        this.symbol.toUpperCase() + (this.market === BOVESPA ? ".SA" : "");

      let { data } = Client(token)
        .post("/api/wallets/" + this.id + "/operations", {
          day: this.day,
          type: this.opType.toLowerCase(),
          quantity: this.quantity,
          value: this.fromText(this.value),
          symbol: parsedSymbol,
        })
        .then(() => {
          this.fetchStocks();
        })
        .catch((error) => {
          console.log(error);
          this.incorrect = true;
        });
    },
    fetchStocks() {
      this.loading = true;
      const token = this.$store.state.token;
      Client(token)
        .get("/api/wallets/" + this.id + "/operations", {})
        .then((response) => {
          this.opHistory = response.data;
        })
        .catch((error) => {
          if (error.response.status === 403) this.unauth = true;
          else this.incorrect = true;
        })
        .finally(() => {
          this.loading = false;
          this.firstLoading = false;
        });
      let currency = i18n.locale === "pt-br" ? "BRL" : "USD";
      console.log(currency);
      Client(token)
        .get("/api/wallets/" + this.id + "/?currency=" + currency, {})
        .then((response) => {
          this.consolidated = response.data.stocks;
          this.currentTotalValue = response.data.current_total_value;
        })
        .catch((error) => {
          if (error.response.status === 403) this.unauth = true;
          else this.incorrect = true;
        })
        .finally(() => {
          this.loading = false;
          this.firstLoading = false;
        });
    },
    async remove(item) {
      const token = this.$store.state.token;
      await Client(token)
        .delete("/api/wallets/" + this.id + "/operations/" + item.id)
        .then(() => {
          this.fetchStocks();
        })
        .catch((error) => {
          console.log(error);
          this.incorrect = true;
        });
    },
    updateMarket(val){
      this.market = val;
      this.marketOptions.buttons.forEach((btn) =>
          btn.value !== val ? (btn.state = false) : null
      );
      this.symbol = '';
    }
  },
  watch: {
    market: function (val) {
      this.companies = val === BOVESPA ? bovespaCompanies : nasdaqCompanies;
    },
  },
};
</script>