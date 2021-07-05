<template>
  <div class="sidebar-menu">
    <b-container fluid class="p-0">
      <h1 class="stocktitle">Stock Scout</h1>
    </b-container>

    <b-container fluid class="logo">
      <img class="logo" src="../assets/logo.png" />
    </b-container>

    <div class="flagcontainer">
      <div class="flag"></div>
      <div class="flagtext">{{ $t("hello") }}, {{ username }}</div>
      <div class="flag">
        <b-dropdown>
          <template #button-content>
            <flag :iso="selectedFlag" v-bind:squared="false" />
          </template>
          <div>
            <b-dropdown-item
              v-for="entry in languages"
              :key="entry.title"
              @click="changeLocale(entry)"
            >
              <flag :iso="entry.flag" v-bind:squared="false" />
              {{ entry.title }}
            </b-dropdown-item>
          </div>
        </b-dropdown>
      </div>
    </div>

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
import i18n from "@/plugins/i18n";

export default {
  data() {
    return {
      loginPage: false,
      signUpPage: false,
      username: "Guest",
      languages: [
        { flag: "us", language: "en", title: "English" },
        { flag: "br", language: "pt-br", title: "Português" },
      ],
      selectedFlag: "us",
    };
  },
  methods: {
    logout() {
      this.$store.commit("removeToken");
      this.$router.push("/");
    },
    changeLocale(locale) {
      i18n.locale = locale.language;
      this.selectedFlag = locale.flag;
      localStorage.setItem("locale", JSON.stringify(locale));
      this.$emit('refresh');
    },
  },
  mounted() {
    let savedLocale = localStorage.getItem("locale");
    if (savedLocale != null) {
      let parsedLocale = JSON.parse(savedLocale);
      if (parsedLocale != null) {
        i18n.locale = parsedLocale.language;
        this.selectedFlag = parsedLocale.flag;
      }
    }

    if (this.$store.getters.isLoggedIn) {
      const token = this.$store.state.token;
      Client(token)
        .get("/api/me/")
        .then((response) => {
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
  font-size: 2.5vw;
  display: flex;
  justify-content: center;
  text-align: center;
}

.navigation {
  font-size: 1.6vw;
  flex-direction: row;
  display: flex;
  justify-content: center;
  text-align: left;
}

.flagcontainer {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-content: center;
  align-items: center;
}

.flag {
  width: 30%;
}

.flagtext {
  align-self: center;
  width: 40%;
}

.logo {
  width: 70%;
}
</style>