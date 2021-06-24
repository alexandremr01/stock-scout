<template>
  <div id="Dashboard">
    <apexcharts ref="Chart" width="70%" type="line" :options="chartOptions" :series="series"></apexcharts>
  </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'

import VueApexCharts from 'vue-apexcharts'

export default {
  name: 'Dashboard',
  components : { 
    apexcharts: VueApexCharts
  },
  data: function() {
    return {
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
    var { data } = await axios.get("http://localhost:8080/api/stocks/?symbol=NDAQ&freq=DAY");
    
    data = JSON.parse(data);
    
    var date_array = [];
    var opening_price_array = [];
    
    data.forEach(data_element => {
      const date = data_element.Date // moment(data_element.Date, "YYYYMMDD").format("DD/MM");
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