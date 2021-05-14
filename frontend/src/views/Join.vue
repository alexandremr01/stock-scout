<template>
  <div>
      <h1>Join! (logo bodosa)</h1>
  <div>
    <button type="button" class="btn btn-primary" @click="$router.push('login')">Login</button>
  </div>
  <div>
    <button type="button" class="btn btn-secondary" @click="$router.push('sign-up')">Signup</button>
  </div>
  </div>
</template>
<script>
export default {
  name: 'Join',
  mounted(){

  }
};
</script>
<style scoped>
</style>