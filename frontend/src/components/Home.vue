<template>
  <v-app id="main-container" v-if="this.$store.state.auth.token">
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
      <v-container>
        <v-col cols="12">
          <bookmark />
        </v-col>
        <v-row>
          <v-col cols="12">
            <search-bar />
          </v-col>
        </v-row>
      </v-container>
    </div>
    <v-container>
      <v-row class="pr-6 pl-6 pb-6">
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
import gsap from "gsap";
import Bookmark from "../views/Bookmark";
import Notepad from "./Notepad.vue";
import SearchBar from "../views/SearchBar";
import { mapActions, mapGetters, mapMutations } from "vuex";
import Calendar from "../views/Calendar";
import Setting from "../views/Setting/Setting.vue";

export default {
  data() {
    return {};
  },
  methods: {
    ...mapActions("auth", ["getUserInfo"]),
    ...mapMutations("settings", { settingsDialog: "dialogToggle" }),
    ...mapGetters("settings", ["settingDialog"]),
    success(position) {
      const lat = position.coords.latitude;
      const lon = position.coords.longitude;
      this.$store.dispatch("weather/getGeoWeather", { lat, lon });
    },
    error() {
      this.$store.dispatch("weather/getResWeather");
    }
  },
  components: {
    Setting,
    Bookmark,
    Notepad,
    SearchBar,
    Calendar
  },
  created() {
    if (navigator.geolocation) {
      console.log(navigator.geolocation);
      navigator.geolocation.getCurrentPosition(this.success, this.error);
      // geolocation API를 브라우저가 지원한다면 실행할 코드
    } else {
      this.$store.dispatch("weather/getResWeather");
    }
  },
  mounted() {
    const tl = gsap.timeline();
    tl.to("#main-container", {
      opacity: 1,
      duration: 1,
      delay: 0.5
    });
  }
};
</script>

<style scoped>
#main-container {
  opacity: 0;
}
</style>
