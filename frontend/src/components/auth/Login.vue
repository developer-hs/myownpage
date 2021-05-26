<template>
  <v-app>
    <v-container fill-height mb-16 style="max-width:850px">
      <v-layout align-center>
        <v-flex xs12>
          <v-alert class="mb-3" :value="isLoginError" type="error">
            아이디와 비밀번호를 확인해주세요.
          </v-alert>
          <v-card>
            <v-toolbar flat>
              <v-toolbar-title>Login</v-toolbar-title>
            </v-toolbar>
            <div class="pa-3">
              <v-form ref="form" v-model="valid" lazy-validation>
                <v-text-field
                  v-model="loginObj.username"
                  :counter="10"
                  :rules="nameRules"
                  @click="isLoginError = false"
                  label="Name"
                  required
                ></v-text-field>
                <v-text-field
                  :rules="passwordRules"
                  :append-icon="passwordShow ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="passwordShow ? 'text' : 'password'"
                  label="Password"
                  @click:append="passwordShow = !passwordShow"
                  @click="isLoginError = false"
                  required
                  v-model="loginObj.password"
                ></v-text-field>
                <v-btn
                  depressed
                  color="success"
                  class="mr-4 border-b"
                  @click="logIn(loginObj)"
                >
                  logIn
                </v-btn>

                <v-btn
                  depressed
                  color="error"
                  class="mr-4"
                  @click="$router.push({ name: 'signup' })"
                >
                  SignUp
                </v-btn>
                <v-btn depressed color="warning" @click="resetValidation">
                  Find Password
                </v-btn>
              </v-form>
            </div>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>
<script>
import { mapActions, mapState } from "vuex";
import { AccessToken } from "../../variable";
import store from "../../store";

export default {
  data() {
    return {
      loginObj: {
        username: "admin",
        password: "admin",
      },
      valid: true,
      nameRules: [
        (v) => !!v || "Name is required",
        (v) => (v && v.length <= 10) || "Name must be less than 10 characters",
      ],
      passwordRules: [
        (v) => !!v || "Password is required",
        (v) => (v && v.length >= 3) || "Passwrod must ba less than 3 integer",
      ],
      passwordShow: "",
    };
  },
  computed: {
    ...mapState({
      isLoginError: (state) => state.auth.isLoginError,
      isLoggedIn: (state) => state.auth.isLoggedIn,
    }),
  },
  methods: {
    ...mapActions("auth", ["logIn"]),
    logOut() {
      store.state.auth.token = null;
      localStorage.removeItem(AccessToken);
    },
    validate() {
      this.$refs.form.validate();
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
  },
};
</script>
<style>
router-link {
  text-decoration: none;
  color: white;
}
</style>
