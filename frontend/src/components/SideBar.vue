<template>
  <div>
    <div>
      <b-container fluid class="profile-picture">
        <b-img
          src="https://picsum.photos/125/125/?image=58"
          rounded="circle"
        ></b-img>
      </b-container>
      <b-container fluid class="navigation">
        <b-nav vertical>
          <b-nav-item to="home">
            <b-icon-house-door-fill
              scale=".6"
              shift-v="-.6"
            ></b-icon-house-door-fill
            >Home</b-nav-item
          >
          <b-nav-item to="profile">
            <b-icon-person-fill scale=".6" shift-v="-.6"></b-icon-person-fill>
            My Profile</b-nav-item
          >
          <b-nav-item to="dashboard">
            <b-icon-graph-up scale=".6" shift-v="-.6"></b-icon-graph-up>
            Dashboard</b-nav-item
          >
          <b-nav-item to="wallets">
            <b-icon-wallet2 scale=".6" shift-v="-.6"></b-icon-wallet2>
            Wallets</b-nav-item
          >
          <b-nav-item to="simulations">
            <b-icon-calculator-fill
              scale=".6"
              shift-v="-.6"
            ></b-icon-calculator-fill>
            Simulations</b-nav-item
          >
        </b-nav>
      </b-container>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loginPage: false,
      signUpPage: false,
    };
  },
  mounted() {
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
.profile-picture {
  padding: 30px;
  height: 25%;
}

.navigation {
  font-size: 20px;
  height: 60%;
  flex-direction: row;
  display: flex;
  justify-content: center;
  text-align: left;
}
</style>