<template>
  <v-app>
    <v-container>
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
        <v-btn color="success" class="login-button mr-4" @click="login">
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
  </v-app>
</template>
<script>
import callApi from "../api/callApi";
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
    };
  },
  methods: {
    login() {
      callApi("post", "/users/login/", {
        username: this.username,
        password: this.password,
      })
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
          if (error.response.status == 401) {
            alert("Username or Password Wrong");
            this.$refs.form.reset();
          }
        });
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
