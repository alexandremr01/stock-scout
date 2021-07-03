<template>
  <div class="outer">
    <b-container fluid class="maincontainer">
      <transition name="enable-sidebar">
        <b-container fluid class="sidebar" v-if="this.homeState">
          <SideBar />
        </b-container>
      </transition>

      <transition name="enable-sidetext"
        ><b-container fluid class="sidetext" v-if="this.loginSignupState">
          <h1 v-if="this.$route.name == `login`">Welcome back!</h1>
          <h1 v-if="this.$route.name == `signup`">Welcome Friend!</h1>
        </b-container></transition
      >

      <b-container fluid class="content">
        <router-view
          @to-login-signup="changeState(`loginSignupPage`)"
          @to-home="changeState(`homePage`)"
          @to-join="changeState(`joinPage`)"
        ></router-view>
      </b-container>
    </b-container>
  </div>
</template>

<script>
import SideBar from "../components/SideBar.vue";

export default {
  data() {
    return {
      sideBarStates: ["joinPage", "loginSignupPage", "dashboardPage"],
      sideBarCurrentState: "joinPage",
      loginSignupState: false,
      homeState: false,
    };
  },
  components: {
    SideBar,
  },
  methods: {
    changeState(toPage) {
      if (toPage == "loginSignupPage") {
        this.sideBarCurrentState = toPage;
        this.loginSignupState = true;
        this.homeState = false;
      } else if (toPage == "homePage") {
        this.sideBarCurrentState = toPage;
        this.loginSignupState = false;
        this.homeState = true;
      } else {
        this.loginSignupState = false;
        this.homeState = false;
      }
    },
  },
};
</script>


<style scoped>
.outer {
  padding: 50px;
}

.maincontainer {
  display: flex;
  align-content: flex-end;
  height: 92vh;
  width: 100%;
  padding: 20px;
  border-radius: 20px;
  background-color: black;
}

.sidebar {
  width: 25%;
  background-color: cornsilk;
  transition-duration: 300ms;
  transition-property: width;
}

.sidetext {
  width: 45%;
  margin: auto;
  background-color: black;
  transition-duration: 300ms;
  transition-property: width;
}

/* .sidetext:hover {
  width: 60%;
} */

.content {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: cadetblue;
}

.enable-sidebar-enter-active,
.enable-sidebar-leave-active {
  transition: width 0.5s ease;
}
.enable-sidebar-enter,
.enable-sidebar-leave-to {
  width: 0;
}

.enable-sidetext-enter-active,
.enable-sidetext-leave-active {
  transition: width 0.5s ease;
}
.enable-sidetext-enter,
.enable-sidetext-leave-to {
  width: 0;
}
</style>