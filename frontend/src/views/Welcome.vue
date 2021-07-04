<template>
  <div class="anthonybg">
    <b-container fluid class="continuecontainer">
      <b-container class="continuetext">
        <h3>A melhor maneira de acompanhar seus investimentos.</h3>
      </b-container>
      <b-button pill class="button" @click="toLogin"
        >Continuar
        <svg width="16" height="16" fill="none" viewBox="0 0 21 20" role="img">
          <g>
            <path
              d="M18.5 10H2.5M18.5 10L12 16.5M18.5 10L12 3.5"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="square"
              stroke-linejoin="round"
            ></path>
          </g></svg
      ></b-button>
    </b-container>
    <b-container fluid class="anthonycontainer">
      <img src="../assets/anthony-resized.png" class="anthony" />
    </b-container>
  </div>
</template>

<script>
export default {
  name: "Welcome",
  methods: {
    toLogin() {
      this.$router.push("/login");
    },
  },
  mounted() {
    if (this.$store.getters.isLoggedIn) this.$router.push("/home");
  },
  data() {
    return {
      backgroundImage: require("../assets/S.svg"),
    };
  },
};
</script>

<style scoped>
.anthonybg {
  width: 100%;
  height: 100%;
  border-radius: 20px;
  background: rgb(234, 243, 243);
  background: linear-gradient(
    to bottom right,
    rgba(234, 243, 243, 1) 0%,
    rgba(203, 214, 208, 1) 35%,
    rgba(190, 205, 206, 1) 100%
  );
}

.anthonycontainer {
  padding-top: 10%;
  padding-right: 5%;
  height: 100%;
}

.anthony {
  width: auto;
  float: right;
  height: 100%;
}

.continuecontainer {
  border-radius: 20px;
  padding: 20px;
  background: #fbfcfc;
  position: fixed;
  top: 50%;
  left: 30%;
  transform: translate(-50%, -50%);
  width: 300px;
  height: 250px;
}

.continuetext {
  text-align: left;
  color: black;
  padding-bottom: 60px;
}

.button {
  width: 80%;
}

.icon {
  width: 100%;
}
</style>