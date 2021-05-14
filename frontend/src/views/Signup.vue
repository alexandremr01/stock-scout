<template>
  <div>
    <h1>Signup Page</h1>

    <b-form @submit="onSubmit" >
      <b-form-group id="input-group-1" label="Username:" label-for="input-1">
        <b-form-input
            id="input-1"
            v-model="form.username"
            placeholder="Enter username"
            required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Email address:" label-for="input-2">
        <b-form-input
            id="input-2"
            v-model="form.email"
            placeholder="Enter email"
            required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Your Password:" label-for="input-3">
        <b-form-input
            id="input-3"
            v-model="form.password"
            placeholder="Enter password"
            type="password"
            required
        ></b-form-input>
      </b-form-group>

      <div v-if="incorrect">
        Usuário ou senha incorreto.
      </div>

      <b-button type="submit" variant="primary" >Sign up</b-button>
    </b-form>
  </div>
</template>
<script>
import Repository from "../repositories/RepositoryFactory";

const RegisterRepository = Repository.get("register");

export default {
  name: 'Signup',
  data() {
    return {
      form: {
        username: '',
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
      RegisterRepository.register(this.form.username, this.form.email, this.form.password)
          .then( (response) => {
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
</style>