<template>
  <div class="button">
    <b-button pill @click="toLogin">Continue</b-button>
  </div>
</template>

<script>
export default {
  name: "Welcome",
  methods: {
    toLogin() {
      this.$emit("to-login-signup");
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
.button {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.icon {
  width: 100%;
}
</style>