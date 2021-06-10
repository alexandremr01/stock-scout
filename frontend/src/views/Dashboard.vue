<template>
  <h1>Dashboard</h1>

</template>

<script>
import axios from 'axios';
export default {
  name: 'Dashboard',
  components : {

  },
  async created() {
    const { data } = await axios.get("http://localhost:8080/api/stocks/?symbol=NDAQ&freq=DAY");
    console.log(data);
  }
};
</script>

<style scoped>

</style>