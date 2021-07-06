<template>
  <div>
    <b-container class="bloco bg-secondary">
      <b-container class="title">
        <h1 class="text-primary">Login</h1>
      </b-container>
      <b-container class="form">
        <b-form @submit="onSubmit" class="form-input">
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
              v-model="form.password"
              placeholder="Enter password"
              type="password"
              required
            ></b-form-input>
          </b-form-group>

          <div v-if="incorrect">Usuário ou senha incorreto.</div>

          <b-container vertical>
            <b-container class="buttons">
              <b-button pill type="submit" variant="success" class="text-primary button"
                >Login</b-button
              >
              <b-button
                pill
                @click="toDashboard"
                variant="success"
                class="text-primary button"
                >{{$t('guestLogin')}}</b-button
              >
            </b-container>
            <b-container class="footer">
              <p>
                {{$t('newToStockScout')}}
                <b-link @click="toSignup">{{$t('signUp')}}</b-link>
              </p>
            </b-container>
          </b-container>
        </b-form>
      </b-container>
    </b-container>
  </div>
</template>

<script>
import Repository from "../repositories/RepositoryFactory";

const TokenRepository = Repository.get("token");

export default {
  name: "Login",
  data() {
    return {
      transition: false,
      form: {
        email: "",
        password: "",
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
      await TokenRepository.obtain(this.form.email, this.form.password)
        .then((response) => {
          this.$store.commit("updateToken", response.data.token);
          this.$router.push("/home");
        })
        .catch((error) => {
          console.log(error);
          this.incorrect = true;
        });
    },
    toSignup() {
      this.$router.push("/sign-up");
    },
    toDashboard() {
      this.$router.push("/home");
    },
  },
};
</script>
<style scoped>
.bloco {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 500px;
  border-radius: 20px;
  padding: 0px 50px;
  margin: auto;
}

.align-label {
  text-align: left;
  padding-bottom: 10px;
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
  display: flex;
  flex-flow: row wrap;
  justify-content: space-between;
  padding-bottom: 10px;
}

.footer {
  padding-bottom: 20px;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 2s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>