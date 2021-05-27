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
        v-for="(site, index) in userInfo.bookmark.sites"
      >
        {{ site.name }}
      </v-btn>
    </div>
  </v-flex>
</template>
<script>
import { mapState } from "vuex";
export default {
  data() {
    return {};
  },
  computed: {
    ...mapState({
      userInfo: (state) => state.auth.userInfo,
    }),
  },
  methods: {
    paintBookmark() {
      const bookmarBar = document.querySelector(".bookmark-bar");
      const bookmark = bookmarBar.childNodes;
      const locked = this.userInfo.bookmark.locked;
      for (let i = 0; i < bookmark.length; i++) {
        if (bookmark[i].innerText === locked) {
          bookmark[i].classList.add(locked.toLowerCase());
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
</style>
