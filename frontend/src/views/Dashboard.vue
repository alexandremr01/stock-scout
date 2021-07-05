<template>
  <div id="Dashboard" class="dashboardcontainer">
    <div class="extremecontainer">
      <div class="addgraphform">
        <div class="stocksearch">
          <v-select
            class="style-chooser"
            @input="searchStock"
            :options="companies"
            v-model="searchText"
            :reduce="(x) => x.symbol"
            label="name"
          ></v-select>
        </div>
        <div class="stockselection">
          <div class="stocktype">
            <b-button-group>
              <b-button
                v-for="(btn, idx) in marketOptions.buttons"
                :key="idx"
                :pressed.sync="btn.state"
                style="fontsize: 16px"
                variant="primary"
                @click="updateMarket(btn.value)"
              >
                <flag :iso="btn.flag" v-bind:squared="false" />&nbsp;{{
                  btn.caption
                }}
              </b-button>
              <b-button
                v-for="(btn, idx) in otherMarketOptions.buttons"
                :key="idx + 2"
                :pressed.sync="btn.state"
                style="fontsize: 16px"
                variant="primary"
                @click="updateMarket(btn.value)"
              >
                <b-icon :icon="btn.icon"></b-icon> {{ btn.caption }}
              </b-button>
            </b-button-group>
          </div>
          <div class="graphtype">
            <b-button
              variant="primary"
              style="fontsize: 16px; width: 135px"
              @click="chartType = chartType === 'line' ? 'candlestick' : 'line'"
            >
              <div v-if="chartType == 'line'">
                <b-icon icon="graph-up" aria-hidden="true"></b-icon>
                Line
              </div>
              <div v-else>
                <b-icon icon="align-middle" aria-hidden="true"></b-icon>
                Candlestick
              </div>
            </b-button>
          </div>
        </div>
      </div>
      <div class="addbutton">
        <b-button variant="primary" @click="getStockData()">Add</b-button>
      </div>
      <!-- 
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
        </b-row>
      </b-container>

      <b-button
        variant="primary"
        style="fontsize: 16px; width: 135px"
        @click="chartType = chartType === 'line' ? 'candlestick' : 'line'"
      >
        <div v-if="chartType == 'line'">
          <b-icon icon="graph-up" aria-hidden="true"></b-icon>
          Line
        </div>
        <div v-else>
          <b-icon icon="align-middle" aria-hidden="true"></b-icon>
          Candlestick
        </div>
      </b-button>

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
        <b-button
          v-for="(btn, idx) in otherMarketOptions.buttons"
          :key="idx + 2"
          :pressed.sync="btn.state"
          style="fontsize: 16px"
          variant="primary"
          @click="updateMarket(btn.value)"
        >
          <b-icon :icon="btn.icon"></b-icon> {{ btn.caption }}
        </b-button>
      </b-button-group>

      <b-col cols="2">
        <b-button variant="primary" @click="getStockData()">Add</b-button>
      </b-col> -->
    </div>
    <div class="middlecontainer">
      <GraphCard
        v-for="chart in charts"
        ref="charts"
        :key="chart.id"
        :chartType="chart.type"
        :stock="chart.stockName"
        :categories="chart.categories"
        :chartSeries="chart.series"
        :id="chart.id"
        v-on:remove="removeChart"
        v-on:changeFrequency="changeChartFrequency"
      >
      </GraphCard>
    </div>
    <div class="extremecontainer"></div>

    <b-spinner label="Loading..." v-if="loading"></b-spinner>
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
const INDEX = "INDEX";

import GraphCard from "../components/GraphCard.vue";
import Client from "../repositories/Clients/AxiosClient";

export default {
  name: "Dashboard",
  components: {
    vSelect,
    GraphCard,
  },
  mounted() {
    this.fetchWallets();
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
      indexOptions: [
        { name: "Selic" },
        { name: "USD" },
        { name: "EUR" },
        { name: "Nasdaq" },
        { name: "Ibovespa" },
        { name: "Bitcoin" },
      ],
      charts: [],
      loading: false,
      error: false,
      marketOptions: {
        buttons: [
          { caption: "BOVESPA", state: true, value: BOVESPA, flag: "br" },
          { caption: "NASDAQ", state: false, value: NASDAQ, flag: "us" },
        ],
      },
      otherMarketOptions: {
        buttons: [
          { caption: "WALLET", state: false, value: WALLET, icon: "wallet" },
          { caption: "INDEX", state: false, value: INDEX, icon: "server" },
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
      axios
        .get(
          "/api/stocks/?symbol=" + parsedSymbol + "&freq=" + this.stockFrequency
        )
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
    },
    changeChartFrequency(id, chartType, stock, frequency) {
      let parsedSymbol = stock + (this.market === BOVESPA ? ".SA" : "");

      this.loading = true;
      axios
        .get("/api/stocks/?symbol=" + parsedSymbol + "&freq=" + frequency)
        .then((response) => {
          this.loading = false;

          let data = response.data;
          data = JSON.parse(data);

          if (chartType == "line") {
            let dateArray = [];
            let closingPriceArray = [];

            data.forEach((dataElement) => {
              const date = dataElement.Date;
              const closingPrice = dataElement.close;

              dateArray.push(date);
              closingPriceArray.push(closingPrice);
            });
            this.$refs.charts[id].changeChartData(dateArray, closingPriceArray);
          }

          if (chartType == "candlestick") {
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
            this.$refs.charts[id].changeChartData(dateArray, dataArray);
          }
        });
    },
    fetchWallets() {
      const token = this.$store.state.token;
      Client(token)
        .get("/api/wallets/", {})
        .then((response) => {
          this.wallets = response.data;
        })
        .catch(() => {
          this.incorrect = true;
        });
    },
  },
  watch: {
    // a computed getter
    market: function (val) {
      if (val === BOVESPA) {
        this.companies = bovespaCompanies;
      } else if (val === NASDAQ) {
        this.companies = nasdaqCompanies;
      } else if (val === WALLET) {
        this.companies = this.wallets;
      } else if (val === INDEX) {
        this.companies = this.indexOptions;
      }
      this.marketOptions.buttons.forEach((btn, index) =>
        btn.value != val ? (btn.state = false) : null
      );
      this.otherMarketOptions.buttons.forEach((btn, index) =>
        btn.value != val ? (btn.state = false) : null
      );
    },
  },
};
</script>

<style>
.dashboardcontainer {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100%;
  width: 100%;
}

.extremecontainer {
  width: 100%;
  height: 15%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}

.middlecontainer {
  width: 100%;
  height: 70%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  flex-wrap: wrap;
  align-items: center;
}

.addgraphform {
  padding-left: 5%;
  padding-right: 5%;
  height: 100%;
  width: 80%;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}
.stocksearch {
}
.stockselection {
  display: flex;
  flex-direction: row;
  justify-content: center;
}
.stocktype {
  align-self: center;
  width: 80%;
}
.graphtype {
  width: 20%;
  align-self: center;
}
.addbutton {
  padding-left: 5%;
  padding-right: 5%;
  height: 100%;
  width: 20%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

/* 
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
} */

.apexcharts-tooltip {
  color: rgb(0, 0, 0);
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