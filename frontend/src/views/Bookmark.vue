<template>
  <v-container>
    <v-row align="center">
      <v-col cols="7">
        <div id="bookmark-bar" class="text-xs-center">
          <v-btn
            depressed
            text
            class="mr-5 font-weight-medium"
            small
            :key="index"
            v-for="(site, index) in bookmark.sites"
            @click="siteLocked(site.name)"
          >
            {{ site.name }}
          </v-btn>
        </div>
      </v-col>
      <v-col cols="5">
        <v-crad>
          <rain v-if="weather === 'Mist' || weather === 'Rain'" />
          <sun v-else-if="weather === ''" />
          <cloud v-else-if="weather === 'Clouds'" />
          <v-row justify="center pt-3 pl-2">
            <span>{{ temp }}°C</span>
          </v-row>
        </v-crad>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import Rain from "./Weather/Rain.vue";
import Cloud from "./Weather/Cloud.vue";
import Sun from "./Weather/Sun.vue";
import { mapActions, mapState } from "vuex";
import gsap from "gsap";
export default {
  components: {
    Rain,
    Sun,
    Cloud
  },
  data() {
    return {};
  },
  computed: {
    ...mapState({
      bookmark: state => state.bookmark.bookmark
    }),
    weather() {
      return this.$store.state.weather.weatherCondition.weather[0].main;
    },
    temp() {
      return this.$store.state.weather.weatherCondition.main.temp;
    }
  },
  methods: {
    ...mapActions("bookmark", ["siteLocked"]),
    siteLocked(siteName) {
      const preSiteName = this.bookmark.locked;
      this.$store.dispatch("bookmark/siteLocked", siteName);
      setTimeout(() => {
        this.paintBookmark(preSiteName);
      }, 50);
    },
    paintBookmark(preSiteName) {
      const bookmarBar = document.querySelector("#bookmark-bar");
      const el_Bookmark = bookmarBar.childNodes;
      const locked = this.bookmark.locked;
      for (let i = 0; i < el_Bookmark.length; i++) {
        if (el_Bookmark[i].innerText === locked) {
          el_Bookmark[i].classList.add(locked.toLowerCase());
        } else if (el_Bookmark[i].innerText === preSiteName) {
          el_Bookmark[i].classList.remove(preSiteName.toLowerCase());
        }
      }
    }
  },

  mounted() {
    console.log("awdjlkajdklawjdkla");
    console.log(this.weather);
    console.log("awdjlkajdklawjdkla");
    this.paintBookmark();
    const tl = gsap.timeline();
    tl.to("#bookmark-bar", {
      duration: 1,
      opacity: 1,
      delay: 0.5
    });
  }
};
</script>
<style scoped>
#bookmark-bar {
  opacity: 0;
}
.daum {
  color: #3498db;
}
.naver {
  color: #27ae60;
}
.google {
  color: #c23616;
}
.yahoo {
  color: #6003d2;
}
.missha {
  color: #686de0;
}
.bing {
  color: #3498db;
}
.duckduckgo {
  color: #fdd309;
}
</style>
