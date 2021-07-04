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
          <b-nav-item to="home">Home</b-nav-item>
          <b-nav-item to="profile">My Profile</b-nav-item>
          <b-nav-item to="dashboard">Dashboard</b-nav-item>
          <b-nav-item to="wallets">Wallets</b-nav-item>
          <b-nav-item to="simulations">Simulations</b-nav-item>
          <b-nav-item @click="logout" v-if="$store.getters.isLoggedIn">Log Out</b-nav-item>
          <b-nav-item to="" v-if="!$store.getters.isLoggedIn">Back</b-nav-item>
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
  methods:{
    logout(){
      this.$store.commit('removeToken');
      this.$router.push('/');
    },
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
  height: 60%;
  flex-direction: row;
  display: flex;
  justify-content: center;
  text-align: center;
}
</style>