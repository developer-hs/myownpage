<template>
  <v-container>
    <v-row>
      <v-col cols="11">
        <div class="bookmark-bar text-xs-center">
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
      <v-col cols="1">
        <v-btn
          icon
          fab
          depressed
          small
          @click="$router.push({ name: 'setting' })"
          ><v-icon>mdi-cog</v-icon>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import { mapActions, mapState } from "vuex";
export default {
  data() {
    return {};
  },
  computed: {
    ...mapState({
      bookmark: state => state.bookmark.bookmark
    })
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
      const bookmarBar = document.querySelector(".bookmark-bar");
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
    this.paintBookmark();
  }
};
</script>
<style scoped>
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
