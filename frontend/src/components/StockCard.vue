<template>
  <div>
    <b-container
      fluid
      vertical
      :class="[
        `stockcard`,
        parseFloat(this.variation) < 0 ? `redcard` : `greencard`,
      ]"
    >
      <b-container fluid vertical class="text">
        <h2>{{ stockname }}</h2>
        <h7>{{ description }}</h7>
      </b-container>
      <b-container fluid vertical class="value">
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
  /* background-image: linear-gradient(
    to bottom right,
    #2f373c,
    rgb(143, 143, 143)
  ); */
  /* background-image: linear-gradient(to bottom right, #11c76f, #55b588); */
  padding: 0;
  box-shadow: 10px 10px 2px 1px rgba(0, 0, 0, 0.2);
}

.redcard {
  background-image: linear-gradient(
    135deg,
    rgb(211, 47, 47) 0%,
    rgb(183, 28, 28) 100%
  );
}

.greencard {
  background-image: linear-gradient(135deg, #1bb31b 0%, #118511 100%);
}

.text {
  color: white;
  padding-top: 5%;
  text-align: left;
  padding-bottom: 10%;
}

.value {
  color: black;
  text-align: left;
  margin: 0;
}
</style>