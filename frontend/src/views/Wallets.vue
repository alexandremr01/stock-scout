<template>
  <div>
    <h1>{{$t('wallets')}}</h1>

    <b-container class="bv-example-row bv-example-row-flex-cols">
      <b-row cols="12">
        <b-col cols="6">
          <b-row class="my-1" align-h="start">
              <b-col sm="4" align="left">{{$t('wDay')}} </b-col>
              <b-col cols="8">     <b-form-datepicker id="example-datepicker" v-model="day" size="sm"></b-form-datepicker></b-col>
          </b-row>
          <b-row class="my-1" align-h="start">
              <b-col sm="4" align="left">{{$t('wQuantity')}} </b-col>
              <b-col cols="8"> <b-form-input v-model="quantity" type="number"></b-form-input> </b-col>
          </b-row>
          <b-row class="my-1" align-h="start">
              <b-col sm="4" align="left">{{$t('wValue')}} </b-col>
            <b-col cols="8"> <b-form-input v-model="value" type="text" :formatter="currencyFormat"></b-form-input> </b-col>
          </b-row>
          <b-row class="my-1" align-h="start">
              <b-col sm="4" align="left">{{$t('wSymbol')}} </b-col>
              <b-col cols="8"> <b-form-input v-model="symbol" type="text"></b-form-input> </b-col>
          </b-row>
          <b-row class="my-1" align-h="center">
            <!--              <b-col sm="4" align="left">{{$t('wType')}} </b-col>-->
            <!--              <b-col cols="8"> <v-select class="style-chooser" :options="operationTypes" v-model="opType"></v-select> </b-col>-->
            <b-form-group>
              <!--              <b-form-radio v-model="type" name="some-radios" value="Buy">Buy</b-form-radio>-->
              <!--              <b-form-radio v-model="type" name="some-radios" value="Sell">Sell</b-form-radio>-->
              <b-form-radio-group
                  id="radio-group-1"
                  v-model="opType"
                  :options="operationTypes"
                  name="radio-options"
              ></b-form-radio-group>
            </b-form-group>
          </b-row>
          <b-row class="my-1" align-h="center">
            <b-button @click="submit"> Submit </b-button>
          </b-row>
        </b-col>
        <b-col cols="6">
          <div class="container-fluid">
            <b-table sticky-header="true"
                     no-border-collapse="true"
                     small fixed dark hover :items="opHistory" :fields="fields">
              <template #cell(actions)="row">
                <b-button variant="danger" size="sm" @click="remove(row.item, row.index, $event.target)" class="mr-1">
                  {{ $t('remove') }}
                </b-button>
              </template>

            </b-table>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<style>
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
</style>

<script>
import i18n from '@/plugins/i18n';
import Client from "../repositories/Clients/AxiosClient";
export default {
  name: "Wallets",
  mounted(){
    this.fetchStocks()
  },
  data() {
    return {
      day: 0,
      opType: "Buy",
      quantity: 0,
      value: 0,
      symbol: '',
      opHistory: [],
      operationTypes: ["Buy", "Sell"],
      fields:[
        {
          key: 'value',
          sortable: true,
          label: "Valor"
        },
        {
          key: 'type',
          sortable: true,
          label: "Tipo"
        },
        {
          key: 'symbol',
          sortable: true,
          label: "Ação"
        },
        {
          key: 'quantity',
          sortable: true,
          label: "Quantidade"
        },
        {
          key: 'day',
          sortable: true,
          label: "Dia"
        },
        { key: 'actions', label: '' }

      ]
    }
  },
  methods: {
    currencyFormat(value) {
      return this.toCurrency(this.toNumber(value) / 100)
    },
    toNumber(n) {
      return Number(n.replace(/[^0-9]+/g, ""));
    },
    toCurrency(n) {
      let currency = i18n.locale === 'pt-br' ? 'BRL' : 'USD';
      return Number(n).toLocaleString('pt-BR', {style: 'currency', currency: currency})
    },
    fromText(n) {
      if (n == null) return null;
      return this.toNumber(n) / 100;
    },
    submit(){
      const token = this.$store.state.token;
      let {data} = Client(token).post('/api/wallets/3/operations', {
        day: this.day,
        type: this.opType.toLowerCase(),
        quantity: this.quantity,
        value: this.fromText(this.value),
        symbol: this.symbol,
      }).then((response) => {
        this.fetchStocks();
      }).catch((error) => {
        console.log(error)
        this.incorrect = true;
      });
    },
    fetchStocks(){
      const token = this.$store.state.token;
      Client(token).get('/api/wallets/3/operations', {}).then((response) => {
        this.opHistory = response.data;
      }).catch((error) => {
        console.log(error)
        this.incorrect = true;
      });
    },
    async remove(item, index, button) {
      const token = this.$store.state.token;
      await Client(token).delete('/api/wallets/3/operations/' + item.id).then((response) => {
        this.fetchStocks();
      }).catch((error) => {
        console.log(error)
        this.incorrect = true;
      });
    },
  }
};
</script>

<style>
</style>