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
          <h1 v-if="this.$route.name === `login`">Welcome Back!</h1>
          <h1 v-if="this.$route.name === `signup`">Welcome, Friend!</h1>
        </b-container></transition
      >

      <b-container fluid class="content">
        <router-view></router-view>
      </b-container>
    </b-container>
  </div>
</template>

<script>
import SideBar from "../components/SideBar.vue";

export default {
  data() {
    return {
      loginSignupState: false,
      homeState: false,
    };
  },
  components: {
    SideBar,
  },
  mounted() {
    this.routeWatcher = this.$watch(
      function () {
        return this.$route;
      },
      function (route) {
        this.loginSignupState =
          route.name === `login` || route.name === `signup`;
        this.homeState =
          route.name !== `login` &&
          route.name !== `signup` &&
          route.name !== `join` &&
          route.name !== `welcome`;
      }
    );
  },
};
</script>


<style scoped>
.outer {
  padding: 50px;
  background-color: #21272b;
}

.maincontainer {
  display: flex;
  align-content: flex-end;
  height: 92vh;
  width: 100%;
  padding: 0px;
  border-radius: 20px;
}

.sidebar {
  width: 25%;
  background-color: #2f373c;
  border-top-left-radius: 20px;
  border-bottom-left-radius: 20px;
  transition-duration: 300ms;
  transition-property: width;
}

.sidetext {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 45%;
  margin: auto;
  color: primary;
  background-color: #2f373c;
  border-top-left-radius: 20px;
  border-bottom-left-radius: 20px;
  transition-duration: 300ms;
  transition-property: width;
}

.content {
  display: flex;
  justify-content: center;
  align-items: center;
  border-top-right-radius: 20px;
  border-bottom-right-radius: 20px;
  background-color: #e1e3e3;
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