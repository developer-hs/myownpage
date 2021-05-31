<template>
  <v-flex>
    <div class="bookmark-bar text-xs-center justify-center">
      <v-btn
        fab
        depressed
        class="mr-3 font-weight-medium"
        small
        color="white"
        :key="index"
        v-for="(site, index) in bookmark.sites"
        @click="siteLocked(site.name)"
      >
        {{ site.name }}
      </v-btn>
    </div>
  </v-flex>
</template>
<script>
import { mapActions, mapState } from "vuex";
export default {
  data() {
    return {};
  },
  computed: {
    ...mapState({
      bookmark: (state) => state.bookmark.bookmark,
    }),
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
    },
  },
  mounted() {
    this.paintBookmark();
  },
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
</style>
