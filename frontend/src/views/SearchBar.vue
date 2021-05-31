<template>
  <div>
    <v-text-field @keypress.enter="onSearch" v-model="searchTerm" class="pt-9">
      <template v-slot:label>
        사이트 <strong>검색</strong>
        <v-icon style="vertical-align: middle">
          mdi-file-find
        </v-icon>
      </template>
    </v-text-field>
    <v-row class="pt-4" align="center">
      <v-chip
        class="ml-2 mt-2"
        :ripple="false"
        :key="index"
        close
        v-for="(history, index) in searchHistory"
        @click:close="removeSearchHistory(history.id)"
      >
        {{ history.search_term }}
      </v-chip>
    </v-row>
  </div>
</template>
<script>
import { mapActions, mapState } from "vuex";
export default {
  data() {
    return {
      searchTerm: "",
    };
  },
  computed: {
    ...mapState({
      sites: (state) => state.bookmark.bookmark.sites,
      locked: (state) => state.bookmark.bookmark.locked,
      searchHistory: (state) => state.search.searchHistory,
    }),
  },
  methods: {
    ...mapActions("search", ["removeSearchHistory"]),
    onSearch() {
      this.$store.dispatch("search/createSearchHistory", this.searchTerm);
      for (let i = 0; i < this.sites.length; i++) {
        if (this.sites[i].name === this.locked) {
          window.open(`${this.sites[i].site_url}${this.searchTerm}`);
        }
      }
    },
  },
};
</script>
