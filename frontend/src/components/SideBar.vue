<template>
  <div class="sidebar-menu">
    <div class="extremecontainer">
      <b-container fluid class="p-0">
        <h1 class="stocktitle">Stock Scout</h1>
      </b-container>

      <b-container fluid class="logo">
        <img class="logo" src="../assets/logo-border.png" />
      </b-container>

      <div class="flagcontainer">
        <div class="flag"></div>
        <div class="flagtext text-primary">{{ $t("hello") }}, {{ username }}</div>
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
    </div>
    <div class="middlecontainer">
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
            {{$t('wallets')}}</b-nav-item
          >
          <b-nav-item to="/simulations">
            <b-icon-calculator-fill
              scale=".6"
              shift-v="-.6"
            ></b-icon-calculator-fill>
            {{$t('simulations')}}</b-nav-item
          >
          <b-nav-item @click="credits">
            <b-icon-people-fill scale=".6" shift-v="-.6"></b-icon-people-fill>
            {{ $t("credits") }}</b-nav-item
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
    <div class="extremecontainer"></div>
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
      username: '',
      languages: [
        { flag: "us", language: "en", title: "English" },
        { flag: "br", language: "pt-br", title: "Português" },
      ],
      selectedFlag: "us",
    };
  },
  methods: {
    credits() {
      this.$router.push("/about");
    },
    logout() {
      this.$store.commit("removeToken");
      this.$router.push("/");
    },
    changeLocale(locale) {
      i18n.locale = locale.language;
      this.selectedFlag = locale.flag;
      localStorage.setItem("locale", JSON.stringify(locale));
      this.username = this.$t('guest');
      this.$emit("refresh");
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
    this.username = this.$t('guest');

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
  display: flex;
  height: 100%;
  flex-direction: column;
  justify-content: space-evenly;
}

.extremecontainer {
  /* background: red; */
  width: 100%;
  height: 30%;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
}

.middlecontainer {
  /* background: blue; */
  width: 100%;
  height: 40%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}

.stocktitle {
  /* background: blue; */
  color: white;
  font-size: 2vw;
  display: flex;
  justify-content: center;
  text-align: center;
}

.navigation {
  font-size: 1.5vw;
  flex-direction: row;
  display: flex;
  justify-content: center;
  text-align: left;
}

.flagcontainer {
  /* background: yellow; */
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
  /* background: green; */
  width: 70%;
}
</style>