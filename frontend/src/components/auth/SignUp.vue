<template>
  <v-app>
    <v-container fill-height mb-16 style="max-width:850px">
      <v-row align-center>
        <v-col cols="12">
          <v-card>
            <div class="pa-3">
              <v-form ref="form" v-model="valid" lazy-validation>
                <v-text-field
                  v-model="firstName"
                  :counter="10"
                  label="First name"
                ></v-text-field>

                <v-text-field
                  v-model="lastName"
                  :counter="10"
                  label="Last name"
                ></v-text-field>

                <v-text-field
                  v-model="username"
                  :counter="10"
                  :rules="nameRules"
                  label="Username"
                  required
                ></v-text-field>

                <v-text-field
                  v-model="email"
                  :rules="emailRules"
                  label="E-mail"
                  required
                ></v-text-field>

                <v-text-field
                  v-model="password"
                  :append-icon="passwordShow ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="passwordShow ? 'text' : 'password'"
                  label="Password"
                  hint="At least 8 characters"
                  @click:append="passwordShow = !passwordShow"
                ></v-text-field>

                <v-btn
                  depressed
                  :disabled="!valid"
                  color="error"
                  class="mr-4"
                  @click="signUp"
                >
                  SignUp
                </v-btn>
              </v-form>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>
<script>
import callApi from "../../api/callApi";
export default {
  data() {
    return {
      valid: true,
      username: "",
      nameRules: [
        v => !!v || "Name is required",
        v => (v && v.length <= 10) || "Name must be less than 10 characters"
      ],
      email: "",
      emailRules: [
        v => !!v || "E-mail is required",
        v => /.+@.+\..+/.test(v) || "E-mail must be valid"
      ],
      password: "",
      passwordShow: false,
      firstName: "",
      lastName: ""
    };
  },

  methods: {
    signUp() {
      callApi("post", "/users/sign-up", {
        username: this.username,
        email: this.email,
        password: this.password,
        first_name: this.firstName,
        last_name: this.lastName
      })
        .then(response => {
          if (response.status === 201) {
            localStorage.setItem("search_bookmark", "NAVER");
          }
        })
        .catch(error => {
          if (error.response.status == 400) {
            alert("동일한 이메일이 존재합니다");
          }
        });
    }
  },
  created() {
    if (this.$store.state.auth.token) {
      this.$router.push({ name: "home" });
    }
  }
};
</script>
