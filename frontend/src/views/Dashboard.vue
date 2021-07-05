<template>
  <div id="Dashboard" class="dashboardcontainer">
    <div class="extremecontainer">
      <div :class="[`topcontainer`, `bg-secondary`]">
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
                @click="
                  chartType = chartType === 'line' ? 'candlestick' : 'line'
                "
              >
                <div v-if="chartType == 'line'">
                  <b-icon icon="graph-up" aria-hidden="true"></b-icon>
                  {{$t('line')}}
                </div>
                <div v-else>
                  <b-icon icon="align-middle" aria-hidden="true"></b-icon>
                  {{$t('candlestick')}}
                </div>
              </b-button>
            </div>
          </div>
        </div>

        <div class="addselection">
          <div class="addbutton">
            <b-button variant="primary" @click="getStockData()">
              <b-icon icon="plus-square"> </b-icon>
              {{ $t('add') }}
            </b-button>
          </div>

          <div class="loadingicon">
            <b-spinner label="Loading..." v-if="loading"></b-spinner>
          </div>
        </div>
      </div>
    </div>
    <div class="middlecontainer">
      <GraphCard
        v-for="chart in charts"
        ref="charts"
        :key="chart.id"
        :chartType="chart.type"
        :marketType="chart.marketType"
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
import Client from "../repositories/Clients/AxiosClient";

export default {
  name: "Dashboard",
  components: {
    vSelect,
    GraphCard,
  },
  mounted() {
    if(this.$store.getters.isLoggedIn) this.fetchWallets();
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
      this.loading = true;
      if (this.market === NASDAQ || this.market === BOVESPA) {
        let parsedSymbol =
          this.stockSymbol + (this.market === BOVESPA ? ".SA" : "");
        axios
          .get(
            "/api/stocks/?symbol=" +
              parsedSymbol +
              "&freq=" +
              this.stockFrequency
          )
          .then((response) => {
            let data = response.data;
            this.loading = false;
            let parsedData = JSON.parse(data);
            this.parseData(parsedData, this.stockSymbol, this.market);
          })
          .catch(() => {
            this.error = true;
            this.loading = false;
          });
      } else if (this.market === WALLET) {
        let walletID = this.searchText;
        const token = this.$store.state.token;
        Client(token)
          .get("/api/wallets/" + walletID + "/history")
          .then((response) => {
            let data = response.data;
            this.loading = false;
            let walletName = this.wallets.filter(
              (x) => x.symbol == this.searchText
            )[0].name;
            let parsedData = JSON.parse(data).map((x) => {
              return { Date: x.day, close: x.value };
            });
            this.parseData(parsedData, walletName, this.market);
          })
          .catch(() => {
            this.error = true;
            this.loading = false;
          });
      }
    },
    parseData(data, title, marketType) {
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
          marketType: marketType,
          stockName: title,
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
          marketType: marketType,
          stockName: title,
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
          this.wallets = response.data.map((x) => {
            return { name: x.name, symbol: x.id };
          });
        })
        .catch(() => {
          this.incorrect = true;
        });
    },
  },
  computed: {
    otherMarketOptions: function () {
      if (this.$store.getters.isLoggedIn) {
        return {
          buttons: [
            {caption: this.$t('WALLET'), state: false, value: WALLET, icon: "wallet"},
          ],
        }
      }
      return {buttons: []}
    }
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
      }
      this.marketOptions.buttons.forEach((btn, index) =>
        btn.value != val ? (btn.state = false) : null
      );
      this.otherMarketOptions.buttons.forEach((btn, index) =>
        btn.value != val ? (btn.state = false) : null
      );
      this.searchText = "";
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
  height: 20%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}

.topcontainer {
  width: 90%;
  height: 90%;
  display: flex;
  border-radius: 20px;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}

.middlecontainer {
  width: 100%;
  height: 60%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
  flex-wrap: wrap;
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

.stockselection {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.stocktype {
}
.graphtype {
}

.addselection {
  height: 100%;
  width: 20%;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
}

.addbutton {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
  width: 50%;
}
.loadingicon {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 30%;
}
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