<template>
  <div id="app">
    <app-navigation></app-navigation>
    <router-view></router-view>
  </div>
</template>

<script>
import AppNavigation from "./components/AppNavigation";
export default {
  name: 'app',
  components: {
    AppNavigation
  }

}
</script>

<style lang="scss">
@import "./styles/common.scss";

#app {
  font-family: Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
