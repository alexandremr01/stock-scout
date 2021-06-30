<template>
  <div id="Dashboard">
    
      <input type="text" v-on:keyup.enter="searchStock" v-model="stockSymbol" placeholder="search" class="searchText"/>

      <b-button variant="success" class="buyStock">Buy</b-button>

      <b-button variant="danger" class="sellStock">Sell</b-button>

      <b-dropdown text="Visualization" variant="primary" class="visualizationMenu" size="sm">
        <b-dropdown-item href="#">Line</b-dropdown-item>
        <b-dropdown-item href="#">Candlestick</b-dropdown-item>
      </b-dropdown>

      <b-button-group class="stockFreqOptions" size="sm">
        <b-button
          v-for="(btn, idx) in stockFreqOptions.buttons"
          :key="idx"
          :pressed.sync="btn.state"
          variant="primary"
          @click="stockFreqOnPress(idx)"
          class = "stockFreqOptionsButton"
        >
        {{ btn.caption }}
        </b-button>
      </b-button-group>

      <div class="Chart">
        <apexcharts ref="Chart" width="80%" type="line" :options="chartOptions" :series="series" class="Chart"></apexcharts>
      </div>
  
  </div>
</template>

<style>
  .searchText {
    display: inline-block;
    position: absolute;
    top: 15%;
    left: 80%;
    font-size: 80%;
    border: none;
    background-color: white;
    outline: none;
  }
  .buyStock {
    display: inline-block;
    position: absolute;
    top: 15%;
    left: 70%;
    box-shadow: none !important;
  }
  .sellStock {
    display: inline-block;
    position: absolute;
    top: 30%;
    left: 70%;
    box-shadow: none !important;
  }
  .Chart {
    display: inline-block;
    position: absolute;
    top: 25%;
    left: 3%;
    width: 80%;
  }
  .stockFreqOptions {
    display: inline-block;
    position: absolute;
    top: 15%;
    left: 25%;
  }
  .stockFreqOptionsButton {
    box-shadow: none !important;
  }
  .visualizationMenu {
    display: inline-block;
    position: absolute;
    top: 15%;
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
      stockSymbol: '',
      stockFreq: '',
      stockFreqOptions: {
        buttons: [
          { caption: 'Daily', state: true},
          { caption: 'Weekly', state: false},
          { caption: 'Monthly', state: false}
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
          decimalsInFloat: 2,
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
    renderChart: async function(stockSymbol, stockFreq) {
      var { data } = await axios.get('/api/stocks/?symbol=' + stockSymbol + '&freq=' + stockFreq);

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
    updateChart: function() {
      return;
    },
    searchStock: function() {
      return this.renderChart(this.stockSymbol, 'DAY');
    },
    stockFreqOnPress(i) {
      this.stockFreqOptions.buttons.forEach((btn, index) => btn.state = i === index);
    }
  },
  beforeMount() {
    this.renderChart('TSLA', 'DAY'); // Initialization config
  }
};
</script>