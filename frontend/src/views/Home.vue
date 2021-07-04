<template>
  <div>
    <b-container class="description">
      <h3>Cotação das principais moedas para o real</h3>
    </b-container>
    <b-container>
      <b-row class="rows">
        <b-col>
          <StockCard
            stockname="BTC"
            description="Bitcoin"
            value="$ 34,639"
            variation="3.29 %"
          />
        </b-col>
        <b-col
          ><StockCard
            stockname="BTC"
            description="Bitcoin"
            value="$ 34,639"
            variation="3.29 %"
        /></b-col>
        <b-col
          ><StockCard
            stockname="BTC"
            description="Bitcoin"
            value="$ 34,639"
            variation="3.29 %"
        /></b-col>
      </b-row>
      <b-row class="rows">
        <b-col>
          <StockCard
            stockname="BTC"
            description="Bitcoin"
            value="$ 34,639"
            variation="3.29 %"
          />
        </b-col>
        <b-col
          ><StockCard
            stockname="BTC"
            description="Bitcoin"
            value="$ 34,639"
            variation="3.29 %"
        /></b-col>
        <b-col
          ><StockCard
            stockname="BTC"
            description="Bitcoin"
            value="$ 34,639"
            variation="3.29 %"
        /></b-col>
      </b-row>
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
.description {
  padding: 50px;
}

.rows {
  padding-bottom: 20px;
}
</style>