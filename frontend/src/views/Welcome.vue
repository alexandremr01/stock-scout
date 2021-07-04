<template>
  <div class="anthonybg">
    <b-container fluid>
      <b-button pill class="button" @click="toLogin">Continue</b-button>
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

.button {
  width: 200px;
  position: fixed;
  top: 50%;
  left: 30%;
  transform: translate(-50%, -50%);
}

.icon {
  width: 100%;
}
</style>