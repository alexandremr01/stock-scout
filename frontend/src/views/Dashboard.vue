<template>
  <div id="Dashboard">
    <b-spinner label="Loading..." v-if="loading"></b-spinner>

    <GraphCard
      v-for="chart in charts"
      :key="chart.id"
      :chartType="chart.type"
      :stock="chart.stockName"
      :categories="chart.categories"
      :chartSeries="chart.series"
      :id="chart.id"
      v-on:remove="removeChart"
    >
    </GraphCard>

    <b-container class="mt-5">
      <b-row>
        <b-col cols="5">
          <v-select
            class="style-chooser"
            @input="searchStock"
            :options="companies"
            v-model="searchText"
            :reduce="(x) => x.symbol"
            label="name"
          ></v-select>
        </b-col>

        <b-col cols="2">
          <b-dropdown size="lm" variant="primary">
            <template #button-content>
              <b-icon icon="bar-chart-fill" aria-hidden="true"></b-icon>
              Visualization
            </template>
            <b-dropdown-item-button @click="updateChartType('line')">
              <b-icon icon="graph-up" aria-hidden="true"></b-icon>
              Line
            </b-dropdown-item-button>
            <b-dropdown-item-button @click="updateChartType('candlestick')">
              <b-icon icon="align-middle" aria-hidden="true"></b-icon>
              Candlestick
            </b-dropdown-item-button>
          </b-dropdown>
        </b-col>
      </b-row>
    </b-container>

    <b-button-group class="mt-5" size="lm">
      <b-button
        v-for="(btn, idx) in marketOptions.buttons"
        :key="idx"
        :pressed.sync="btn.state"
        style="fontsize: 16px"
        variant="primary"
        @click="updateMarket(btn.value)"
      >
        <flag :iso="btn.flag" v-bind:squared="false" />&nbsp;{{ btn.caption }}
      </b-button>
      <b-button>
        <b-icon icon="wallet" style="fontsize: 16px" variant="primary"></b-icon>
        Wallet
      </b-button>
    </b-button-group>

    <b-col cols="2">
      <b-button variant="primary" @click="getStockData()">Add</b-button>
    </b-col>
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

<script>
import axios from "axios";
import nasdaqCompanies from "../data/nasdaq.json";
import bovespaCompanies from "../data/bovespa.json";
import vSelect from "vue-select";
const BOVESPA = "BOVESPA";
const NASDAQ = "NASDAQ";
const WALLET = "WALLET";

import GraphCard from "../components/GraphCard.vue";

export default {
  name: "Dashboard",
  components: {
    vSelect,
    GraphCard,
  },
  data: function () {
    return {
      companies: bovespaCompanies,
      market: BOVESPA,
      stockSymbol: "PETR4", // initial value
      stockFrequency: "DAY", // initial value
      searchText: "",
      chartType: "line",
      chartCounter: 0,
      charts: [],
      loading: false,
      error: false,
      marketOptions: {
        buttons: [
          { caption: "BOVESPA", state: true, value: BOVESPA, flag: "br" },
          { caption: "NASDAQ", state: false, value: NASDAQ, flag: "us" },
        ],
      },
    };
  },
  methods: {
    getStockData: async function () {
      console.log(this.chartType);
      console.log(this.stockSymbol);

      this.loading = true;

      let parsedSymbol =
        this.stockSymbol + (this.market === BOVESPA ? ".SA" : "");
      axios.get("/api/stocks/?symbol=" + parsedSymbol + "&freq=" + this.stockFrequency)
        .then((response) => {
          let data = response.data;
          this.loading = false;

          data = JSON.parse(data);

          if (this.chartType == "line") {
            let dateArray = [];
            let closingPriceArray = [];

            data.forEach((dataElement) => {
              const date = dataElement.Date;
              const closingPrice = dataElement.close;

              dateArray.push(date);
              closingPriceArray.push(closingPrice);
            });
            this.charts.push({
              type: this.chartType,
              stockName: this.stockSymbol,
              categories: dateArray,
              series: [
                {
                  data: closingPriceArray,
                },
              ],
              id: this.chartCounter,
            });
          }

          if (this.chartType == "candlestick") {
            let dateArray = [];
            let dataArray = [];

            data.forEach((dataElement) => {
              const date = dataElement.Date;
              const openingPrice = dataElement.open;
              const closingPrice = dataElement.close;
              const highPrice = dataElement.high;
              const lowPrice = dataElement.low;

              dateArray.push(date);
              dataArray.push({
                x: date,
                y: [openingPrice, highPrice, lowPrice, closingPrice],
              });
            });
            this.charts.push({
              type: this.chartType,
              stockName: this.stockSymbol,
              categories: dateArray,
              series: [
                {
                  data: dataArray,
                },
              ],
              id: this.chartCounter,
            });
          }
          this.chartCounter += 1;
        })
        .catch(() => {
          this.error = true;
          this.loading = false;
        });
    },
    searchStock: function () {
      this.stockSymbol = this.searchText.toUpperCase();
    },
    updateChartType: function (newType) {
      this.chartType = newType;
    },
    updateMarket(mkt) {
      this.market = mkt;
    },
    removeChart(id) {
      let index = this.charts.findIndex((chart) => chart.id === id);
      this.charts.splice(index, 1);
    }
  },
  watch: {
    // a computed getter
    market: function (val) {
      this.companies = val === BOVESPA ? bovespaCompanies : nasdaqCompanies;
    },
  },
  beforeMount() {},
};
</script>

<style>
.dashboardcontainer {
  display: flex;
  flex-direction: column;
  justify-content: center;
  background: blue;
  width: 100%;
  height: 100%;
}

.graphcontainer {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  background: red;
  width: 100%;
  height: auto;
}

.right-chart-container {
  display: inline-block;
  position: absolute;
  left: 60%;
  top: 10%;
}
.right-chart-options {
  display: inline-block;
  position: absolute;
  left: 61%;
  top: 15%;
}
.right-chart-buy-sell {
  display: inline-block;
  position: absolute;
  top: 18%;
  left: 87%;
}
.buyStock {
  display: inline-block;
  box-shadow: none !important;
}
.sellStock {
  display: inline-block;
  box-shadow: none !important;
}
.Chart {
  display: inline-block;
  position: absolute;
  top: 25%;
  left: 35%;
  width: 70%;
}
.lineChartFrequencyOptions {
  display: inline-block;
  position: absolute;
  top: 70%;
  left: 68%;
}
.lineChartFrequencyOptionsButton {
  box-shadow: none !important;
}
.candlestickChart {
  display: inline-block;
  position: absolute;
  top: 25%;
  left: 14%;
  width: 70%;
}
.apexcharts-tooltip {
  color: darkred;
}

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