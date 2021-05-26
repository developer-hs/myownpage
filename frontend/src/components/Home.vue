<template>
  <v-app v-if="this.$store.state.auth.token">
    <v-form class="pt-5" id="search-form" @submit="onSearch">
      <v-container>
        <bookmark />
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
import Bookmark from "../views/Bookmark";
import { mapActions } from "vuex";
export default {
  data() {
    return {
      searchTerm: "",
    };
  },

  methods: {
    ...mapActions("auth", ["logOut", "getUserInfo"]),
    onSearch() {
      window.open(
        `https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=${this.searchTerm}`
      );
    },
  },
  components: {
    Bookmark,
  },
};
</script>
