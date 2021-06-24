<template>
  <div>
    <h1>{{ $t('pageNotFound') }}</h1>
    <div>
      <button type="button" class="btn btn-primary" @click="$router.push('/')"> {{ $t('backToHome') }}</button>
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