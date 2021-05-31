<template>
  <v-app v-if="this.$store.state.auth.token">
    <v-container>
      <div class="d-flex">
        <v-row>
          <bookmark />
        </v-row>
        <v-row class="justify-end">
          <v-btn
            fab
            depressed
            small
            color="white"
            @click="$router.push({ name: 'setting' })"
            ><v-icon>mdi-cog</v-icon>
          </v-btn>
        </v-row>
      </div>
      <search-bar />
    </v-container>
    <v-container class="d-flex">
      <v-btn @click="logOut">LogOut</v-btn>
      <v-layout>
        <notepad />
      </v-layout>
    </v-container>
  </v-app>
</template>
<script>
import Bookmark from "../views/Bookmark";
import Notepad from "../views/Notepad";
import SearchBar from "../views/SearchBar";
import { mapActions } from "vuex";

export default {
  data() {
    return {};
  },
  methods: {
    ...mapActions("auth", ["logOut", "getUserInfo"]),
  },
  components: {
    Bookmark,
    Notepad,
    SearchBar,
  },
};
</script>
