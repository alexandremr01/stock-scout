<template>
  <div>
    <b-container fluid class="p-0">
      <h1 class="stocktitle">Stock Scout</h1>
    </b-container>
    <b-container fluid class="profile-picture">
      <b-img
        src="https://picsum.photos/125/125/?image=58"
        rounded="circle"
      ></b-img>
    </b-container>
    Olá, {{ username }}
    <b-container fluid class="navigation">
      <b-nav vertical class="navigation">
        <b-nav-item to="/home">
          <b-icon-house-door-fill
            scale=".6"
            shift-v="-.6"
          ></b-icon-house-door-fill>
          Home</b-nav-item
        >
        <b-nav-item to="/dashboard">
          <b-icon-graph-up scale=".6" shift-v="-.6"></b-icon-graph-up>
          Dashboard</b-nav-item
        >
        <b-nav-item to="/wallets" v-if="$store.getters.isLoggedIn">
          <b-icon-wallet2 scale=".6" shift-v="-.6"></b-icon-wallet2>
          Wallets</b-nav-item
        >
        <b-nav-item to="/simulations">
          <b-icon-calculator-fill
            scale=".6"
            shift-v="-.6"
          ></b-icon-calculator-fill>
          Simulations</b-nav-item
        >
        <b-nav-item @click="logout" v-if="$store.getters.isLoggedIn">
          <b-icon-arrow-return-left
            scale=".6"
            shift-v="-.6"
          ></b-icon-arrow-return-left>
          Log Out</b-nav-item
        >
        <b-nav-item to="" v-if="!$store.getters.isLoggedIn">
          <b-icon-arrow-return-left
            scale=".6"
            shift-v="-.6"
          ></b-icon-arrow-return-left>
          Back</b-nav-item
        >
      </b-nav>
    </b-container>
  </div>
</template>

<script>
import Client from "../repositories/Clients/AxiosClient";

export default {
  data() {
    return {
      loginPage: false,
      signUpPage: false,
      username: 'Guest'
    };
  },
  methods: {
    logout() {
      this.$store.commit("removeToken");
      this.$router.push("/");
    },
  },
  mounted() {
    if (this.$store.getters.isLoggedIn){
      const token = this.$store.state.token;
      Client(token).get('/api/me/').then((response)=>{
        this.username = response.data.name;
      });
    }
    this.routeWatcher = this.$watch(
      function () {
        return this.$route;
      },
      function (route) {
        console.log(route.name);
        if (route.name == "login") {
          this.loginPage = true;
        } else if (route.name == "signup") {
          this.signUpPage = true;
        } else {
          this.loginPage = false;
          this.signUpPage = false;
        }
      }
    );
  },
};
</script>

<style scoped>
.stocktitle {
  padding-top: 30px;
  padding-bottom: 30px;
  font-size: 2.5vw;
  display: flex;
  justify-content: center;
  text-align: center;
}

.profile-picture {
  padding-bottom: 30px;
  height: 30%;
}

.navigation {
  font-size: 1.6vw;
  flex-direction: row;
  display: flex;
  justify-content: center;
  text-align: left;
}
</style>