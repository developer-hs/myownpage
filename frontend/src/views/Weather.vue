<template>
  <v-card class="d-flex justify-center align-center flex-column" flat>
    <span class="text-subtitle-2">{{ residence }}</span>
    <rain v-if="weather === 'Mist' || weather === 'Rain'" />
    <sun v-else-if="weather === 'Clear'" />
    <cloud v-else-if="weather === ''" />
    <test v-else-if="weather === 'Clouds'" />
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
  }
};
</script>
