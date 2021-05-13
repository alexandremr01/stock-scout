<template>

<div>
<b-navbar toggleable="lg" type="dark" variant="dark">
  <b-navbar-brand href="#">StockScout</b-navbar-brand>

  <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

  <b-collapse id="nav-collapse" is-nav>
    <b-navbar-nav>
      <b-nav-item to="/">Home</b-nav-item>
      <b-nav-item to="dashboard" v-if="isLoggedIn">Dashboard</b-nav-item>
      <b-nav-item to="about">About</b-nav-item>
    </b-navbar-nav>

    <!-- Right aligned nav items -->
    <b-navbar-nav class="ml-auto">

      <b-nav-item-dropdown text="Lang" right>
        <b-dropdown-item href="#">EN</b-dropdown-item>
        <b-dropdown-item href="#">ES</b-dropdown-item>
        <b-dropdown-item href="#">RU</b-dropdown-item>
        <b-dropdown-item href="#">FA</b-dropdown-item>
      </b-nav-item-dropdown>

      <b-nav-item-dropdown right  v-if="isLoggedIn">
        <!-- Using 'button-content' slot -->
        <template #button-content>
          <em>{{ $store.state.user }}</em>
        </template>
        <b-dropdown-item href="#">Profile</b-dropdown-item>
        <b-dropdown-item @click="logout">Sign Out</b-dropdown-item>
      </b-nav-item-dropdown>
    </b-navbar-nav>
  </b-collapse>
</b-navbar>
</div>
</template>

<script>
export default {
  name: 'AppNavigation',
  computed : {
    isLoggedIn : function(){ return this.$store.getters.isLoggedIn},
    username: 'Usuario'
  },
  methods: {
    logout(){
      this.$store.commit('removeToken');
      this.$router.push('/join');
    }
  }

};
</script>
