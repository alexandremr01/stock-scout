<template>
  <div class="homecontainer">
    <div class="extremecontainer">
      <h3>Cotação das principais moedas para o real</h3>
    </div>
    <div class="middlecontainer">
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
    </div>
    <div class="extremescontainer"></div>
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
  align-items: center;
  height: 100%;
  width: 100%;
}

.extremecontainer {
  width: 100%;
  height: 10%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.middlecontainer {
  width: 100%;
  height: 80%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  flex-flow: row wrap;
  align-items: center;
}
</style>