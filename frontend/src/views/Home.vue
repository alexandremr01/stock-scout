<template>
  <div class="homecontainer">
    <b-container class="description">
      <h3>Cotação das principais moedas para o real</h3>
    </b-container>

    <b-container class="cardcontainer">
      <StockCard
        stockname="BTC"
        description="Bitcoin"
        value="$ 34,639"
        variation="3.29 %"
      />
      <StockCard
        stockname="BTC"
        description="Bitcoin"
        value="$ 34,639"
        variation="3.29 %"
      />
      <StockCard
        stockname="BTC"
        description="Bitcoin"
        value="$ 34,639"
        variation="3.29 %"
      />
      <StockCard
        stockname="BTC"
        description="Bitcoin"
        value="$ 34,639"
        variation="3.29 %"
      />
      <StockCard
        stockname="BTC"
        description="Bitcoin"
        value="$ 34,639"
        variation="3.29 %"
      />
      <StockCard
        stockname="BTC"
        description="Bitcoin"
        value="$ 34,639"
        variation="3.29 %"
      />
      <StockCard
        stockname="BTC"
        description="Bitcoin"
        value="$ 34,639"
        variation="3.29 %"
      />
      <StockCard
        stockname="BTC"
        description="Bitcoin"
        value="$ 34,639"
        variation="3.29 %"
      />
    </b-container>
  </div>
</template>

<script>
import StockCard from "../components/StockCard.vue";

export default {
  components: { StockCard },
  name: "Home",
};
</script>
<style scoped>
.homecontainer {
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;
}

.cardcontainer {
  width: 100%;
  height: 80%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  flex-flow: row wrap;
  align-items: flex-start;
}

.description {
  padding: 10%;
  height: 20%;
}
</style>