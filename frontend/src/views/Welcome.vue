<template>
  <div class="anthonybg">
    <img src="../assets/logo-border.png" class="logo" />
    <div class="anthonyphoto">
      <container class="continuecontainer">
        <container class="continuetext">
          <h3>A melhor maneira de acompanhar seus investimentos.</h3>
        </container>
        <b-button pill class="button" @click="toLogin"
          >Continuar
          <svg
            width="16"
            height="16"
            fill="none"
            viewBox="0 0 21 20"
            role="img"
          >
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
      </container>
    </div>
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

.anthonyphoto {
  display: flex;
  width: 100%;
  height: 100%;
  background-image: url("../assets/anthony-adjusted.png");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: right bottom;
}

.continuecontainer {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  border-radius: 20px;
  padding: 20px;
  background: #fbfcfc;
  align-self: center;
  margin-left: 20%;
  width: 300px;
  height: 250px;
}

.continuetext {
  text-align: left;
  color: black;
}

.button {
  align-self: center;
  width: 80%;
}

.icon {
  width: 100%;
}

.logo {
  position: absolute;
  padding: 10px;
  top: 60px;
  left: 60px;
  width: 90px;
  height: 90px;
}
</style>