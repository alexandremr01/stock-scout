<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <h1>Phrases from Django API:</h1>
    <p
      v-for="(phrase, index) in phrases_from_api"
      :key="index"
    >
      {{ phrase }}
    </p>
    <button type="button" class="btn btn-primary" @click="fetchPhrases">Fetch Phrases</button>

  </div>
</template>

<script>
import Repository from "./repositories/RepositoryFactory";
const PhraseRepository = Repository.get("phrase");


export default {
  name: 'app',

  data: function() {
    return {
      phrases_from_api: [],
    }
  },

  methods: {
    async fetchPhrases() {
      const response = await PhraseRepository.get();
      this.phrases_from_api = response.data.data;
    }
  }

}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
