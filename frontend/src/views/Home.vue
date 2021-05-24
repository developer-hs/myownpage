<template>
  <v-app>
    <v-form class="pt-5" id="search-form" @submit="onSearch">
      <v-container>
        <v-btn small fab text color="green">NAVER</v-btn>
        <v-text-field v-model="searchTerm">
          <template v-slot:label>
            사이트 <strong>검색</strong>
            <v-icon style="vertical-align: middle">
              mdi-file-find
            </v-icon>
          </template>
        </v-text-field>
      </v-container>
    </v-form>
    <v-row>
      <v-btn class="ml-9" @click="logOut">logout</v-btn>
    </v-row>
  </v-app>
</template>
<script>
import { AccessToken } from "../variable";
export default {
  data() {
    return {
      searchTerm: "",
    };
  },
  methods: {
    onSearch() {
      window.open(
        `https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=${this.searchTerm}`
      );
    },
    logOut() {
      this.$store.state.auth.token = null;
      localStorage.removeItem(AccessToken);
      document.location.reload();
    },
  },
  created() {
    if (!this.$store.state.auth.token) {
      this.$router.push("/login");
    }
  },
};
</script>
