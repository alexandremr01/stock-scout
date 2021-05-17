<template>
  <div>
    <h1>Page Not Foud</h1>
    <div>
      <button type="button" class="btn btn-primary" @click="$router.push('/')">Back to home</button>
    </div>
  </div>
</template>
<script>
export default {
  name: 'NotFound',
  mounted(){

  }
};
</script>
<style scoped>
</style>