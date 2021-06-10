<template>
  <v-app v-if="this.$store.state.auth.token">
    <bookmark />
    <search-bar />
    <v-container>
      <v-row>
        <v-col cols="6">
          <calendar />
        </v-col>
        <v-col cols="6">
          <notepad />
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>
<script>
import Bookmark from "../views/Bookmark";
import Notepad from "../views/Notepad";
import SearchBar from "../views/SearchBar";
import { mapActions } from "vuex";
import Calendar from "../views/Calendar";

export default {
  data() {
    return {};
  },
  methods: {
    ...mapActions("auth", ["getUserInfo"])
  },
  components: {
    Bookmark,
    Notepad,
    SearchBar,
    Calendar
  }
};
</script>
