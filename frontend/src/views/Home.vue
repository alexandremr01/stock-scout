<template>
  <div class="homecontainer">
    <div class="extremecontainer">
      <h1 class="text-secondary">{{ $t("homeMessage") }}</h1>
    </div>
    <div class="middlecontainer">
      <div class="rowcontainer">
        <StockCard stockname="Selic" :description="$t('selic')" :value="selic" />
        <StockCard stockname="CDI" :description="$t('cdi')" :value="cdi" />
        <StockCard stockname="BOVA" description="Ibovespa" :value="ibovespa" />
        <StockCard stockname="NASDAQ" description="Nasdaq" :value="nasdaq" />
      </div> 
      <div class="rowcontainer">
        <StockCard
          stockname="USD"
          description="Dólar"
          :value="usd"
          :variation="usd_var"
        />
        <StockCard
          stockname="EUR"
          description="Euro"
          :value="eur"
          :variation="eur_var"
        />
        <StockCard
          stockname="BTC"
          description="Bitcoin"
          :value="btc"
          :variation="btc_var"
        />
      </div>
    </div>
    <div class="extremescontainer"></div>
  </div>
</template>

<script>
import StockCard from "../components/StockCard.vue";
import Client from "../repositories/Clients/AxiosClient";
import axios from "axios";

export default {
  components: { StockCard },
  name: "Home",
  mounted() {
    this.fetchData();
  },
  data() {
    return {
      indexes: {},
      selic: 0.0,
      cdi: 0.0,
      ibovespa: 0.0,
      usd: 0.0,
      btc: 0.0,
      eur: 0.0,
      nasdaq: 0.0,
      usd_var: 0.0,
      eur_var: 0.0,
      btc_var: 0.0,
    };
  },
  methods: {
    fetchData() {
      axios
        .get("/api/index/")
        .then((response) => {
          let indexes = response.data["indexes"];
          let usd = response.data["usd"];
          let eur = response.data["eur"];
          let bitcoin = response.data["btc"];

          this.selic = indexes["selic"] + " %";
          this.cdi = indexes["cdi"] + " %";
          this.nasdaq = indexes["nasdaq"];
          this.ibovespa = indexes["ibovespa"];

          this.usd = this.toCurrency(usd["sell"]);
          this.usd_var = usd["variation"] + " %";
          this.btc = this.toCurrency(bitcoin["sell"]);
          this.btc_var = bitcoin["variation"] + " %";
          this.eur = this.toCurrency(eur["sell"]);
          this.eur_var = eur["variation"] + " %";
        })
        .catch(() => {
          this.incorrect = true;
        });
    },
    toCurrency(n) {
      return Number(n).toLocaleString("pt-BR", {
        style: "currency",
        currency: "BRL",
      });
    },
  },
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
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
}

.rowcontainer {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-evenly;
}
</style>