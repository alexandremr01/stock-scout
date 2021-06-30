<template>
  <div id="Dashboard">
    
      <input type="text" oninput="refresh" v-model="searchText" placeholder="search" class="searchText"/>

      <b-button variant="success" class="addStock">Add</b-button>

      <b-button-group class="optionsMenu">
        <b-button :pressed=true>Daily</b-button>
        <b-button>Weekly</b-button>
        <b-button>Monthly</b-button>
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
  }
  .addStock {
    display: inline-block;
    position: absolute;
    top: 15%;
    left: 70%;
  }
  .Chart {
    display: inline-block;
    position: absolute;
    top: 25%;
    left: 3%;
    width: 80%;
  }
  .optionsMenu {
    display: inline-block;
    position: absolute;
    top: 15%;
    left: 25%;
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
      searchText: '',
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
            text: 'Price ($)'
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
  async created() {
    var { data } = await axios.get("/api/stocks/?symbol=TSLA&freq=DAY");

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
  }
};
</script>