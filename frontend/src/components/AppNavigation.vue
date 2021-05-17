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

      <b-nav-item-dropdown right>
        <template #button-content>
          <flag :iso="selectedFlag" v-bind:squared=false />
        </template>
        <div>
          <b-dropdown-item v-for="entry in languages" :key="entry.title" @click="changeLocale(entry)">
            <flag :iso="entry.flag" v-bind:squared=false /> {{entry.title}}
          </b-dropdown-item>
        </div>
      </b-nav-item-dropdown>

      <b-nav-item-dropdown right  v-if="isLoggedIn">
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
import i18n from '@/plugins/i18n';

export default {
  name: 'AppNavigation',
  computed : {
    isLoggedIn : function(){ return this.$store.getters.isLoggedIn},
    username: 'Usuario'
  },
  data() {
    return {
      languages: [
        { flag: 'us', language: 'en', title: 'English' },
        { flag: 'br', language: 'pt-br', title: 'Português' }
      ],
      selectedFlag:  'us'
    };
  },
  methods: {
    logout(){
      this.$store.commit('removeToken');
      this.$router.push('/join');
    },
    changeLocale(locale) {
      i18n.locale = locale.language;
      this.selectedFlag = locale.flag;
    }
  }

};
</script>
