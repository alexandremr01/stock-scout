<template>
  <div>
    <b-form @submit="onSubmit">
      <b-form-group id="input-group-1" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="graph.stockName"
          placeholder="Enter Stock Name"
          required
        ></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-2" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="graph.chartType"
          placeholder="Enter Chart Type"
          required
        ></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-3" label-for="input-3">
        <b-form-input
          id="input-3"
          v-model="graph.categories"
          placeholder="Enter Categories"
          required
        ></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-4" label-for="input-4">
        <b-form-input
          id="input-4"
          v-model="graph.chartSeries[0].data"
          placeholder="Enter Chart Series Data"
          required
        ></b-form-input>
      </b-form-group>
      <b-button pill type="submit" variant="success" class="button"
        >Add Graph</b-button
      >
    </b-form>
  </div>
</template>

<script>
export default {
  name: "AddGraph",
  data() {
    return {
      graph: {
        chartType: "line",
        stockName: "Stock Name",
        categories: [],
        chartSeries: [
          {
            data: [],
          },
        ],
      },
    };
  },
  methods: {
    onSubmit(e) {
      e.preventDefault();

      if (!this.stockName) {
        alert("add stock");
        return;
      }

      const newGraph = {
        id: Math.floor(Math.random() * 10000),
        chartType: this.chartType,
        stockName: this.stockName,
        categories: this.categories,
        chartSeries: this.chartSeries,
      };

      console.log(newGraph);

      this.chartType = "line";
      this.stockName = "Stock Name";
      this.categories = [];
      this.chartSeries = [
        {
          data: [],
        },
      ];
    },
  },
};
</script>

<style>
</style>