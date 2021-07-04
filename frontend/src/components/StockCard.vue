<template>
  <div>
    <b-container vertical class="stockcard">
      <b-container vertical class="text">
        <h2>{{ stockname }}</h2>
        <h7>{{ description }}</h7>
      </b-container>
      <b-container vertical class="value">
        <h4>{{ value }}</h4>
        <h7>{{ variation }}</h7>
      </b-container>
    </b-container>
  </div>
</template>

<script>
export default {
  name: "StockCard",
  props: ["stockname", "description", "value", "variation"],
};
</script>

<style scoped>
.stockcard {
  height: 220px;
  width: 200px;
  border-radius: 10px;
  background-image: linear-gradient(
    to bottom right,
    rgb(255, 201, 101),
    orange
  );
  padding: 0;
  box-shadow: 10px 10px 2px 1px rgba(0, 0, 0, 0.2);
}

.text {
  color: white;
  padding-top: 10px;
  text-align: left;
  padding-bottom: 20px;
}

.value {
  text-align: left;
  margin: 0;
}
</style>