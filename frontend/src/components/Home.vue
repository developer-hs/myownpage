<template>
  <v-app v-if="this.$store.state.auth.token">
    <v-btn
      style="position:absolute"
      icon
      fab
      depressed
      small
      @click="settingsDialog(true)"
      ><v-icon>mdi-cog</v-icon>
    </v-btn>
    <div id="search-container">
      <rain-drop />
      <v-col cols="12">
        <bookmark />
      </v-col>
      <search-bar />
    </div>
    <v-container style="height:46rem">
      <v-row>
        <v-col cols="12">
          <v-card elevation="1">
            <v-row class="pl-3">
              <v-col cols="6">
                <calendar />
              </v-col>
              <v-col cols="6">
                <notepad />
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <setting />
  </v-app>
</template>
<script>
import Bookmark from "../views/Bookmark";
import Notepad from "./Notepad.vue";
import SearchBar from "../views/SearchBar";
import { mapActions, mapGetters, mapMutations } from "vuex";
import Calendar from "../views/Calendar";
import Setting from "../views/Setting/Setting.vue";
import RainDrop from "../views/partial/WeatherEffect/RainDrop.vue";
export default {
  data() {
    return {};
  },
  methods: {
    ...mapActions("auth", ["getUserInfo"]),
    ...mapMutations("settings", { settingsDialog: "dialogToggle" }),
    ...mapGetters("settings", ["settingDialog"])
  },
  components: {
    RainDrop,
    Setting,
    Bookmark,
    Notepad,
    SearchBar,
    Calendar
  },
  created() {
    navigator.geolocation.getCurrentPosition(position => {
      console.log("위도 : " + position.coords.latitude);
      console.log("경도 : " + position.coords.longitude);
    });
  }
};
</script>
<style scoped>
#search-container {
  background-color: gray;
  left: 0;
  right: 0;
  top: 0;
}
</style>
