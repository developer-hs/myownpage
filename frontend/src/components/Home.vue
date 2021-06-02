<template>
  <v-app v-if="this.$store.state.auth.token">
    <v-container>
      <div class="d-flex">
        <v-row>
          <bookmark />
        </v-row>
        <v-row class="justify-end">
          <v-btn
            icon
            fab
            depressed
            small
            @click="$router.push({ name: 'setting' })"
            ><v-icon>mdi-cog</v-icon>
          </v-btn>
        </v-row>
      </div>
      <search-bar />
    </v-container>
    <v-container class="d-flex">
      <v-layout class="pt-3" justify-center>
        <v-col cols="12" md="8" style="left:20">
          <calendar />
        </v-col>
        <v-col cols="12" md="8">
          <notepad />
        </v-col>
      </v-layout>
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
    ...mapActions("auth", ["getUserInfo"]),
  },
  components: {
    Bookmark,
    Notepad,
    SearchBar,
    Calendar,
  },
};
</script>
