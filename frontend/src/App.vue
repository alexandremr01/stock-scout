<template>
  <div id="app">
    <MainContainer />
  </div>
</template>

<script>
import MainContainer from "./containers/MainContainer.vue";
export default {
  name: "app",
  components: {
    MainContainer,
  },
};
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
