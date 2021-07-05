<template>
  <div class="sidebar-menu">
    <container fluid class="p-0">
      <h1 class="stocktitle">Stock Scout</h1>
    </container>

    <container fluid class="logo">
      <b-img
        src="https://picsum.photos/125/125/?image=58"
        rounded="circle"
      ></b-img>
    </container>

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
          <flag :iso="entry.flag" v-bind:squared="false" /> {{ entry.title }}
        </b-dropdown-item>
      </div>
    </b-dropdown>
    <br />
    {{ $t("hello") }}, {{ username }}

    <container fluid class="navigation">
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
    </container>
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
    },
  },
  mounted() {
    let savedLocale = localStorage.getItem("locale");
    if (savedLocale != null) {
      let parsedLocale = JSON.parse(savedLocale);
      if (parsedLocale != null) this.changeLocale(parsedLocale);
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
.sidebar-menu {
  padding-top: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  height: 50%;
}

.stocktitle {
  font-size: 2.5vw;
  text-align: center;
}

.user {
  font-size: 1.2vw;
  text-align: center;
  color: primary;
}

.logo {
}

.navigation {
  font-size: 1.6vw;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-self: center;
  text-align: left;
}
</style>