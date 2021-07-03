<template>
  <div>
    <h1>Signup Page</h1>

    <b-form @submit="onSubmit" >
      <b-form-group id="input-group-1" label="Email address:" label-for="input-1">
        <b-form-input
            id="input-1"
            v-model="form.email"
            placeholder="Enter email"
            required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="First name:" label-for="input-2">
        <b-form-input
            id="input-2"
            v-model="form.firstName"
            placeholder="Enter first name"
            required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Last name:" label-for="input-3">
        <b-form-input
            id="input-3"
            v-model="form.lastName"
            placeholder="Enter last name"
            required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-4" label="Phone number:" label-for="input-4">
        <b-form-input
            id="input-4"
            v-model="form.phoneNumber"
            placeholder="Enter phone number"
            required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-5" label="Your Password:" label-for="input-5">
        <b-form-input
            id="input-5"
            v-model="form.password"
            placeholder="Enter password"
            type="password"
            required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-6" label="Confirm password:" label-for="input-6">
        <b-form-input
            id="input-6"
            v-model="form.confirmPassword"
            placeholder="Confirm password"
            type="password"
            required
        ></b-form-input>
      </b-form-group>

      <div v-if="incorrect">
        Algo de errado aconteceu.
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
        email: '',
        firstName: '',
        lastName: '',
        phoneNumber: '',
        password: '',
        confirmPassword: ''
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
      RegisterRepository.register(this.form)
          .then( () => {
            this.$router.push('/login');
        }).catch( (error) => {
            if (error.response.hasOwnProperty('data')) {
              if (error.response.data.hasOwnProperty('email')) {
                console.log(error.response.data.email[0])
              }
            } else {
              console.log('something went wrong')
            }
            this.incorrect = true;
        });
    }
  }
};
</script>
<style scoped>
</style>