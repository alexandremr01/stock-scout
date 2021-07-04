<template>
  <div>
    <b-container fluid class="bloco bg-secondary">
      <b-container class="title">
        <h1>Signup</h1>
      </b-container>

      <b-container class="form">
        <b-form @submit="onSubmit">
          <b-form-group
            class="align-label"
            id="input-group-1"
            label-for="input-1"
          >
            <b-form-input
              id="input-1"
              v-model="form.email"
              placeholder="Enter email"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group
            class="align-label"
            id="input-group-2"
            label-for="input-2"
          >
            <b-form-input
              id="input-2"
              v-model="form.firstName"
              placeholder="Enter first name"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group
            class="align-label"
            id="input-group-3"
            label-for="input-3"
          >
            <b-form-input
              id="input-3"
              v-model="form.lastName"
              placeholder="Enter last name"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group
            class="align-label"
            id="input-group-4"
            label-for="input-4"
          >
            <b-form-input
              id="input-4"
              v-model="form.phoneNumber"
              placeholder="Enter phone number"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group
            class="align-label"
            id="input-group-5"
            label-for="input-5"
          >
            <b-form-input
              id="input-5"
              v-model="form.password"
              placeholder="Enter password"
              type="password"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group
            class="align-label"
            id="input-group-6"
            label-for="input-6"
          >
            <b-form-input
              id="input-6"
              v-model="form.confirmPassword"
              placeholder="Confirm password"
              type="password"
              required
            ></b-form-input>
          </b-form-group>

          <div v-if="incorrect">Algo de errado aconteceu.</div>

          <b-container class="buttons">
            <b-button pill type="submit" variant="success" class="button"
              >Signup</b-button
            >
          </b-container>

          <b-container class="footer">
            <p>
              Already a member?
              <b-link @click="toLogin">Login</b-link>
            </p>
          </b-container>
        </b-form>
      </b-container>
    </b-container>
  </div>
</template>
<script>
import Repository from "../repositories/RepositoryFactory";

const RegisterRepository = Repository.get("register");

export default {
  name: "Signup",
  data() {
    return {
      form: {
        email: "",
        firstName: "",
        lastName: "",
        phoneNumber: "",
        password: "",
        confirmPassword: "",
      },
      incorrect: false,
    };
  },
  mounted() {
    this.incorrect = false;
  },
  methods: {
    async onSubmit(event) {
      event.preventDefault();
      RegisterRepository.register(this.form)
        .then(() => {
          this.$router.push("/login");
        })
        .catch((error) => {
          if (error.response.hasOwnProperty("data")) {
            if (error.response.data.hasOwnProperty("email")) {
              console.log(error.response.data.email[0]);
            }
          } else {
            console.log("something went wrong");
          }
          this.incorrect = true;
        });
    },
    toLogin() {
      this.$router.push("/login");
    },
  },
};
</script>
<style scoped>
.bloco {
  width: 500px;
  border-radius: 20px;
  margin: auto;
  padding: 0px 50px;
}

.align-label {
  text-align: left;
  padding-bottom: 10px;
}

.form-input {
}

.button {
  width: 150px;
}

.title {
  padding: 20px;
}

.form {
  align-items: center;
}

.buttons {
  padding-bottom: 10px;
}

.footer {
  padding-bottom: 20px;
}
</style>