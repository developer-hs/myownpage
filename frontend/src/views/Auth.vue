<template>
  <v-app>
    <v-container v-if="!token">
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-text-field
          v-model="username"
          :counter="10"
          :rules="nameRules"
          label="Name"
          required
        ></v-text-field>

        <v-text-field
          :rules="passwordRules"
          label="Password"
          required
          v-model="password"
        ></v-text-field>
        <v-btn color="success" class="login-button mr-4" @click="logIn">
          logIn
        </v-btn>

        <v-btn color="error" class="mr-4" @click="reset">
          SignUp
        </v-btn>

        <v-btn color="warning" @click="resetValidation">
          Find Password
        </v-btn>
      </v-form>
    </v-container>
    <v-container v-if="token">
      <v-btn @click="logOut">Logout</v-btn>
    </v-container>
  </v-app>
</template>
<script>
import callApi from "../api/callApi";
import store from "../store";

export default {
  data() {
    return {
      username: "",
      password: "",
      valid: true,
      nameRules: [
        (v) => !!v || "Name is required",
        (v) => (v && v.length <= 10) || "Name must be less than 10 characters",
      ],
      passwordRules: [
        (v) => !!v || "Password is required",
        (v) => (v && v.length >= 3) || "Passwrod must ba less than 3 integer",
      ],
      token: this.$store.state.auth.token,
    };
  },

  methods: {
    logIn() {
      callApi("post", "/users/login/", {
        username: this.username,
        password: this.password,
      })
        .then((response) => {
          if (response.status === 200) {
            store.commit("auth/setToken", response.data.token);
          }
        })
        .catch((error) => {
          console.log(error);
          if (error.response.status == 401) {
            alert("Username or Password Wrong");
            this.$refs.form.reset();
          }
        });
    },
    logOut() {
      this.$store.state.auth.token = null;
      localStorage.removeItem("access_token");
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
  updated() {
    console.log(this.$store.state.auth.token);
  },
};
</script>
