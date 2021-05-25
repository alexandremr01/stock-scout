<template>
  <div>
    <div>
      <h1>{{ $t('join') }}</h1>
      <img :src="backgroundImage" class="icon"/>

    </div>

    <b-row>
      <b-col>
        <b-button variant="primary" @click="$router.push('login')">{{ $t('login') }}</b-button>
      </b-col>
      <b-col>
        <b-button variant="secondary" @click="$router.push('sign-up')">{{ $t('signup') }}</b-button>
      </b-col>
      <b-col>
        <b-button variant="secondary" @click="$router.push('dashboard')">{{ $t('guest') }}</b-button>
      </b-col>
    </b-row>
  </div>
</template>
<script>

export default {
  name: 'Join',
  mounted() {
    if (this.$store.getters.isLoggedIn)
      this.$router.push('/home')
  },
  data(){
    return {
      backgroundImage: require('../assets/S.svg')
    }
  }

};
</script>
<style >
.icon {
  width: 100%;
}
</style>