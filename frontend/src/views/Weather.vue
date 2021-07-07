<template>
  <v-card class="d-flex justify-center align-center flex-column" flat>
    {{ residence }}
    <rain v-if="weather === 'Mist' || weather === 'Rain'" />
    <sun v-else-if="weather === 'Clear'" />
    <cloud v-else-if="weather === 'Clouds'" />
    <test v-else-if="weather === ''" />
    <span class="pt-2 text-caption">{{ temp }}°C</span>
  </v-card>
</template>
<script>
import Rain from "./Weather/RainDrop.vue";
import Cloud from "./Weather/Clouds.vue";
import Sun from "./Weather/Sun.vue";
import Test from "../components/Test";
export default {
  components: {
    Rain,
    Sun,
    Cloud,
    Test
  },
  methods: {
    success(position) {
      const lat = position.coords.latitude;
      const lon = position.coords.longitude;
      this.$store.dispatch("weather/getGeoWeather", { lat, lon });
      console.log("위도 : " + position.coords.latitude);
      console.log("경도 : " + position.coords.longitude);
    },
    error() {
      this.$store.dispatch("weather/getResWeather");
    }
  },
  computed: {
    weather() {
      return this.$store.state.weather.weatherCondition.weather[0].main;
    },
    temp() {
      return this.$store.state.weather.weatherCondition.main.temp;
    },
    residence() {
      return this.$store.state.weather.weatherCondition.name;
    }
  },
  created() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(this.success, this.error);
      // geolocation API를 브라우저가 지원한다면 실행할 코드
    } else {
      this.$store.dispatch("weather/getResWeather");
    }
  }
};
</script>
