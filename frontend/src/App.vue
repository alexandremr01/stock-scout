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

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
