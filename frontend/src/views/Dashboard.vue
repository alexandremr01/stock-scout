<template>
  <div id="Dashboard">


    <b-row align-h="start">
      <b-col cols="4">
        <v-select class="style-chooser" @input="searchStock" :options="companies" v-model="searchText" :reduce="x => x.symbol" label="name"></v-select>
      </b-col>

<!--      <b-col cols="4">-->
<!--      <b-input-group size="lm" class="searchBar">-->
<!--        <b-input-group-prepend is-text>-->
<!--          <b-icon icon="search"></b-icon>-->
<!--        </b-input-group-prepend>-->
<!--        <b-form-input list="company-list" type="text" v-on:keyup.enter="searchStock" v-model="searchText" placeholder="search for stocks"></b-form-input>-->
<!--        <datalist id="company-list">-->
<!--          <option v-for="company in companies"> {{ company.name }} - {{company.symbol}} </option>-->
<!--        </datalist>-->
<!--      </b-input-group>-->
<!--      </b-col>-->

      <b-col cols="4">
        <b-button variant="success" class="buyStock" size="lm">
          <b-icon icon="bag-plus-fill" aria-hidden="true"></b-icon>&nbsp;Buy
        </b-button>
        <b-button variant="danger" class="sellStock" size="lm">
          <b-icon icon="bag-x-fill" aria-hidden="true"></b-icon>&nbsp;Sell
        </b-button>
      </b-col>



      <b-col cols="4">
        <b-button-group class="" size="lm">
          <b-button
              v-for="(btn, idx) in marketOptions.buttons"
              :key="idx"
              :pressed.sync="btn.state"
              variant="primary"
              @click="updateMarket(btn.value)">
            <flag :iso="btn.flag" v-bind:squared=false />&nbsp;{{ btn.caption }}
          </b-button>
        </b-button-group>
      </b-col>
    </b-row>

    <b-button-group class="lineChartFrequencyOptions" size="lm">
        <b-button
          v-for="(btn, idx) in lineChartFrequencyOptions.buttons"
          :key="idx"
          :pressed.sync="btn.state"
          variant="primary"
          @click="lineChartFrequencyOnPress(idx)"
          class = "lineChartFrequencyOptionsButton"
        >
        <b-icon :icon=btn.icon></b-icon>&nbsp;{{ btn.caption }}
        </b-button>
      </b-button-group>

      <div class="Chart">
        <lineChart ref="Chart" width="75%" type="line" :options="lineChartOptions" :series="lineChartSeries" class="Chart"></lineChart>
      </div>

      <div class="candlestickChart">
        <candlestickChart ref="candlestickChart" width="75%" type="candlestick" :options="candlestickChartOptions" :series="candlestickChartSeries" class="candlestickChart"></candlestickChart>
      </div>
  
  </div>
</template>

<style>
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
    top: 15%;
    left: 26%;
    width: 75%;
  }
  .lineChartFrequencyOptions {
    display: inline-block;
    position: absolute;
    top: 70%;
    left: 58%;
  }
  .lineChartFrequencyOptionsButton {
    box-shadow: none !important;
  }
  .candlestickChart {
    display: inline-block;
    position: absolute;
    top: 15%;
    left: 0%;
    width: 75%;
  }
  .apexcharts-tooltip {
    color: darkred
  }


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
import axios from 'axios'
import nasdaqCompanies from '../data/nasdaq.json';
import bovespaCompanies from '../data/bovespa.json';
import VueApexCharts from 'vue-apexcharts'
import vSelect from 'vue-select'
const BOVESPA = 'BOVESPA';
const NASDAQ = 'NASDAQ';

export default {
  name: 'Dashboard',
  components : { 
    lineChart: VueApexCharts,
    candlestickChart: VueApexCharts,
    vSelect,
  },
  data: function() {
    return {
      companies: bovespaCompanies,
      market: BOVESPA,
      stockSymbol: 'PETR4', // initial value
      stockFrequency: 'DAY', // initial value
      searchText: '',
      lineChartFrequencyOptions: {
        buttons: [
          { caption: 'Daily', state: true, frequency: 'DAY', icon: 'calendar3-event'},
          { caption: 'Weekly', state: false, frequency: 'WEEK', icon: 'calendar3-week'},
          { caption: 'Monthly', state: false, frequency: 'MONTH', icon: 'calendar3'}
        ]
      },
      marketOptions: {
        buttons: [
          { caption: 'Bovespa', state: true, value: BOVESPA, flag: 'br'},
          { caption: 'Nasdaq', state: false, value: NASDAQ, flag: 'us'}
        ]
      },
      lineChartOptions: {
        chart: {
          toolbar: {
            show: false
          }
        },
        colors: ['#cc5d18'], // @todo
        dataLabels: {
          enabled: true, // todo: add button to enable/disable
          style: {
            fontSize: '12px',
          }
        },
        xaxis: {
          categories: [],
          type: 'datetime',
          labels: {
            format: 'dd MMM',
            style: {
              colors: '#ffffff',
              fontSize: '16px',
            }
          }
        },
        yaxis: {
          decimalsInFloat: 0,
          labels: {
            style: {
              colors: '#ffffff',
              fontSize: '16px',
            }
          },
          title: {
            text: 'Closing Price',
            style: {
              color: '#ffffff',
              fontSize: '18px',
            }
          }
        },
        stroke: {
          curve: 'smooth',
          width: 3
        },
        theme: {
          mode: 'light',
        },
        title: {
          text: 'TSLA',
          align: 'center',
          offsetY: 10,
          style: {
            fontSize: '18px',
            fontWeight: 'bold',
            color: '#ffffff'
          }
        },
        tooltip: {
          custom: function({series, seriesIndex, dataPointIndex, w}) {
            return '<div class="arrow_box">' +
              '<span>' + series[seriesIndex][dataPointIndex] + '\ USD' + '</span>' +
              '</div>'
          }
        }
      },
      candlestickChartOptions: {
        chart: {
          toolbar: {
            show: false
          }
        },
        colors: ['#cc5d18'], // @todo
        xaxis: {
          categories: [],
          type: 'datetime',
          labels: {
            format: 'dd MMM',
            style: {
              colors: '#ffffff',
              fontSize: '16px',
            }
          }
        },
        yaxis: {
          decimalsInFloat: 0,
          labels: {
            style: {
              colors: '#ffffff',
              fontSize: '16px',
            }
          },
          title: {
            text: 'Price',
            style: {
              color: '#ffffff',
              fontSize: '18px',
            }
          }
        },
        stroke: {
          curve: 'smooth',
          width: 3
        },
        theme: {
          mode: 'light',
        },
        title: {
          text: 'TSLA',
          align: 'center',
          offsetY: 10,
          style: {
            fontSize: '18px',
            fontWeight: 'bold',
            color: '#ffffff'
          }
        }
      },
      lineChartSeries: [{
        data: []
      }],
      candlestickChartSeries: [{
        data: []
      }]
    };
  },
  methods: {
    renderChart: async function(stockSymbol, stockFrequency) {
      let parsedSymbol = stockSymbol + (this.market === BOVESPA? '.SA' : '');
      let { data } = await axios.get('/api/stocks/?symbol=' + parsedSymbol + '&freq=' + stockFrequency);

      data = JSON.parse(data);

      let dateArray = [];
      let closingPriceArray = [];
      let candlestickArray = [];
      
      data.forEach(dataElement => {
        const date = dataElement.Date
        const openingPrice = dataElement.open;
        const closingPrice = dataElement.close;
        const highPrice = dataElement.high;
        const lowPrice = dataElement.low;

        dateArray.push(date);
        closingPriceArray.push(closingPrice);
        candlestickArray.push({x: date, y: [openingPrice, highPrice, lowPrice, closingPrice]});
      });
      
      this.renderLineChart(dateArray, closingPriceArray);
      this.renderCandlestickChart(dateArray, candlestickArray);
    },
    renderLineChart: function(date, openingPrice) {
      this.lineChartOptions.xaxis.categories = date.reverse();
      this.lineChartSeries.data = openingPrice.reverse();

      console.log(this.stockSymbol)

      this.$refs.Chart.updateOptions({
        series: [{
          data: this.lineChartSeries.data
        }],
        xaxis: {
          categories: this.lineChartOptions.xaxis.categories
        },
        title: {
          text: this.stockSymbol
        }
      })
    },
    renderCandlestickChart: function(date, data) {
      this.candlestickChartOptions.xaxis.categories = date.reverse();
      this.candlestickChartSeries.data = data.reverse();

      this.$refs.candlestickChart.updateOptions({
        series: [{
          data: this.candlestickChartSeries.data
        }],
        xaxis: {
          categories: this.candlestickChartOptions.xaxis.categories
        },
        title: {
          text: this.stockSymbol
        }
      })
    },
    changeChartFrequency: function(stockFrequency) {
      return this.renderChart(this.stockSymbol, stockFrequency);
    },
    searchStock: function() {
      this.stockSymbol = this.searchText.toUpperCase();
      console.log(this.stockSymbol);
      console.log(this.searchText);
      return this.renderChart(this.stockSymbol, this.stockFrequency);
    },
    lineChartFrequencyOnPress(i) {
      this.lineChartFrequencyOptions.buttons.forEach((btn, index) => btn.state = i === index);
      this.lineChartFrequencyOptions.buttons.forEach((btn, index) => (i === index) ? this.changeChartFrequency(btn.frequency) : null);
      this.lineChartFrequencyOptions.buttons.forEach((btn, index) => (i === index) ? this.stockFrequency = btn.frequency : null);
    },
    updateMarket(mkt) {
      this.market = mkt;
    }
  },
  watch: {
    // a computed getter
    market: function (val) {
      this.companies = val === BOVESPA? bovespaCompanies : nasdaqCompanies;
    }
  },
  beforeMount() {
    this.renderChart(this.stockSymbol, this.stockFrequency);
  }
};
</script>