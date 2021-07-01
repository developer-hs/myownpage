<template>
  <v-card class="d-flex justify-center align-center flex-column" flat>
    <svg width="80" height="20">
      <text
        text-anchor="middle"
        alignment-baseline="middle"
        transform="translate(40, 10)"
        fill="#000000"
        font-size="15"
        font-family="'Leckerli One', cursive"
        letter-spacing="1"
      >
        {{ residence }}
      </text>
    </svg>
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
