<template>
  <div id="dashboard" class="container">
    <div class="row mt-5" v-if="opening_price.length > 0">
      <div class="col">
        <h2>Opening Price</h2>
        <line-chart :chart_data="opening_price" :options="chart_options" label="Opening"></line-chart>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import moment from 'moment';

import LineChart from '../components/LineChart'

export default {
  name: 'Dashboard',
  components : { 
    LineChart
  },
  data() {
    return {
      opening_price: [],
      closing_price: [],
      chart_options: {
        responsive: true,
        maintain_aspect_ratio: false
      }
    };
  },
  async created() {
    var { data } = await axios.get("http://localhost:8080/api/stocks/?symbol=NDAQ&freq=DAY");
    
    // console.log(data);

    data = JSON.parse(data);

    data.forEach(data_element => {
      const date = moment(data_element.Date, "YYYYMMDD").format("DD/MM");
      const opening = data_element.open;
      const closing = data_element.close;

      this.opening_price.push({date, price : opening});
      this.closing_price.push({date, price : closing});
    });
    console.log(this.opening_price);
  }
};
</script>

<style scoped>

</style>