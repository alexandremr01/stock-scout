<template>
  <div class="bloco bg-primary">
    <h1>Login</h1>

    <b-form @submit="onSubmit" class="bloco-input">
      <b-form-group class="align-label"
          id="input-group-1"
          label="Email address:"
          label-for="input-1"
      >
        <b-form-input 
            id="input-1"
            v-model="form.email"
            placeholder="Enter email"
            required
        ></b-form-input>
      </b-form-group>

      <b-form-group class="align-label"
          id="input-group-2" label="Your Password:" label-for="input-2">
        <b-form-input
            id="input-2"
            v-model="form.password"
            placeholder="Enter password"
            type="password"
            required
        ></b-form-input>
      </b-form-group>

      <div v-if="incorrect">
        Usuário ou senha incorreto.
      </div>
      <b-button type="submit" variant="success" class="largura-botao">Login</b-button>
      <b-button @click="$router.push('/')" variant="success" class="largura-botao">{{ $t('back') }}</b-button>
    </b-form>
  </div>
</template>
<script>
import Repository from "../repositories/RepositoryFactory";

const TokenRepository = Repository.get("token");

export default {
  name: 'Login',
  data() {
    return {
      form: {
        email: '',
        password: ''
      },
      incorrect: false,
    }
  },
  mounted() {
    this.incorrect = false;
  },
  methods: {
    async onSubmit(event) {
      event.preventDefault()
      await TokenRepository.obtain(this.form.email, this.form.password)
          .then( (response) => {
            this.$store.commit('updateToken', response.data.token)
            this.$router.push('/');
        }).catch( (error) => {
            console.log(error)
            this.incorrect = true;
        });
    }
  }
};
</script>
<style scoped>

.bloco {
  width: 500px;
  height: 100%;
  border-radius: 20px;
  margin: 100px auto;
  padding: 20px;
}

.bloco-imput {
  width: 70%;
  margin: 20px auto;
}

.align-label{
  text-align: left;
  padding-bottom: 30px;
}

.largura-botao {
  width: 150px;
}

</style>