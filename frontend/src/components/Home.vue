<template>
  <v-app v-if="this.$store.state.auth.token">
    <v-col cols="12">
      <v-btn
        style="position:absolute"
        icon
        fab
        depressed
        small
        @click="$router.push({ name: 'setting' })"
        ><v-icon>mdi-cog</v-icon>
      </v-btn>
      <bookmark />
    </v-col>
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
import Notepad from "./Notepad.vue";
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
