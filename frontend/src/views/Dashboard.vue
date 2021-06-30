<template>
  <div id="Dashboard">

      <b-input-group size="sm" class="mt-4" style="width: 15%; left: 80%;">
        <b-input-group-prepend is-text>
          <b-icon icon="search"></b-icon>
        </b-input-group-prepend>
        <b-form-input type="text" v-on:keyup.enter="searchStock" v-model="searchText" placeholder="search"></b-form-input>
      </b-input-group>

      <b-button variant="success" class="buyStock" size="sm">
        <b-icon icon="bag-plus-fill" aria-hidden="true"></b-icon>
      </b-button>

      <b-button variant="danger" class="sellStock" size="sm">
        <b-icon icon="bag-x-fill" aria-hidden="true"></b-icon>
      </b-button>

      <b-dropdown class="visualizationMenu" size="sm" variant="primary">
        <template #button-content>
          <b-icon icon="bar-chart-fill" aria-hidden="true"></b-icon> Visualization
        </template>
        <b-dropdown-item-button>
          <b-icon icon="graph-up" aria-hidden="true"></b-icon>
          Line
        </b-dropdown-item-button>
        <b-dropdown-item-button>
          <b-icon icon="align-middle" aria-hidden="true"></b-icon>
          Candlestick
        </b-dropdown-item-button>
      </b-dropdown>

      <b-button-group class="stockFrequencyOptions" size="sm">
        <b-button
          v-for="(btn, idx) in stockFrequencyOptions.buttons"
          :key="idx"
          :pressed.sync="btn.state"
          variant="primary"
          @click="stockFrequencyOnPress(idx)"
          class = "stockFrequencyOptionsButton"
        >
        <b-icon :icon=btn.icon></b-icon>&nbsp;{{ btn.caption }}
        </b-button>
      </b-button-group>

      <div class="Chart">
        <apexcharts ref="Chart" width="80%" type="line" :options="chartOptions" :series="series" class="Chart"></apexcharts>
      </div>
  
  </div>
</template>

<style>
  .buyStock {
    display: inline-block;
    position: absolute;
    top: 85%;
    left: 47%;
    box-shadow: none !important;
  }
  .sellStock {
    display: inline-block;
    position: absolute;
    top: 85%;
    left: 52%;
    box-shadow: none !important;
  }
  .Chart {
    display: inline-block;
    position: absolute;
    top: 15%;
    left: 3%;
    width: 80%;
  }
  .stockFrequencyOptions {
    display: inline-block;
    position: absolute;
    top: 85%;
    left: 24%;
  }
  .stockFrequencyOptionsButton {
    box-shadow: none !important;
  }
  .visualizationMenu {
    display: inline-block;
    position: absolute;
    top: 85%;
    left: 10%;
    box-shadow: none !important;
  }
</style>

<script>
import axios from 'axios'

import VueApexCharts from 'vue-apexcharts'

export default {
  name: 'Dashboard',
  components : { 
    apexcharts: VueApexCharts
  },
  data: function() {
    return {
      stockSymbol: 'TSLA', // initial value
      stockFrequency: 'DAY', // initial value
      searchText: '',
      stockFrequencyOptions: {
        buttons: [
          { caption: 'Daily', state: true, frequency: 'DAY', icon: 'calendar3-event'},
          { caption: 'Weekly', state: false, frequency: 'WEEK', icon: 'calendar3-week'},
          { caption: 'Monthly', state: false, frequency: 'MONTH', icon: 'calendar3'}
        ]
      },
      chartOptions: {
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
            format: 'dd MMM'
          }
        },
        yaxis: {
          decimalsInFloat: 0,
          title: {
            text: 'Price (USD)'
          }
        },
        stroke: {
          curve: 'smooth',
          width: 3
        },
        theme: {
          mode: 'light',
        },
      },
      series: [{
        data: []
      }]
    };
  },
  methods: {
    renderChart: async function(stockSymbol, stockFrequency) {
      var { data } = await axios.get('/api/stocks/?symbol=' + stockSymbol + '&freq=' + stockFrequency);

      data = JSON.parse(data);
    
      var date_array = [];
      var opening_price_array = [];
    
      data.forEach(data_element => {
        const date = data_element.Date
        const opening = data_element.open;
      
        date_array.push(date);
        opening_price_array.push(opening);
      });
      this.chartOptions.xaxis.categories = date_array.reverse();
      this.series.data = opening_price_array.reverse();

      this.$refs.Chart.updateOptions({
        series: [{
          data: this.series.data
        }],
        xaxis: {
          categories: this.chartOptions.xaxis.categories
        }
      })
    },
    changeChartFrequency: function(stockFrequency) {
      return this.renderChart(this.stockSymbol, stockFrequency);
    },
    searchStock: function() {
      this.stockSymbol = this.searchText.toUpperCase();
      return this.renderChart(this.stockSymbol, this.stockFrequency);
    },
    stockFrequencyOnPress(i) {
      this.stockFrequencyOptions.buttons.forEach((btn, index) => btn.state = i === index);
      this.stockFrequencyOptions.buttons.forEach((btn, index) => (i === index) ? this.changeChartFrequency(btn.frequency) : null);
      this.stockFrequencyOptions.buttons.forEach((btn, index) => (i === index) ? this.stockFrequency = btn.frequency : null);
    }
  },
  beforeMount() {
    this.renderChart(this.stockSymbol, this.stockFrequency);
  }
};
</script>