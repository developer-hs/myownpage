<template>
  <v-flex>
    <div class="text-xs-center justify-center">
      <v-btn
        fab
        depressed
        class="mr-3 font-weight-medium"
        small
        color="white"
        :key="i"
        v-for="(d, i) in userInfo.bookmark.sites"
        @click="onSelectSite"
      >
        {{ d.name }}
      </v-btn>
    </div>
  </v-flex>
</template>
<script>
import { mapState } from "vuex";
export default {
  data() {
    return {
      fixedSite: "NAVER",
      preSelectNode: "",
      selectNode: "",
    };
  },
  computed: {
    ...mapState({
      userInfo: (state) => state.auth.userInfo,
      select: (state) => state.auth.select,
    }),
  },
  methods: {
    onSelectSite(value) {
      console.log(value.target.childNodes.length);
      this.userInfo.bookmark.sites.forEach((site) => {
        if (value.target.childNodes.length === 1) {
          console.log(site);
          this.selectNode = value.target.parentNode;
        } else {
          this.selectNode = value.target;
        }
      });
      if (this.preSelectNode) {
        this.preSelectNode.classList.remove("green", "lighten-3");
      }
      localStorage.setItem("search_bookmark", this.selectNode.innerText);
      this.selectNode.className += " green lighten-3";
      this.preSelectNode = this.selectNode;
    },
  },
};
</script>
