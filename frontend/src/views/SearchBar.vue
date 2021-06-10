<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-text-field
          @keypress.enter="onSearch"
          v-model="searchTerm"
          class="pt-9"
        >
          <template v-slot:label>
            사이트 <strong>검색</strong>
            <v-icon style="vertical-align: middle">
              mdi-file-find
            </v-icon>
          </template>
        </v-text-field>
      </v-col>
      <v-col cols="12">
        <v-chip
          outlined
          class="ml-2 mt-2"
          :ripple="false"
          :key="index"
          close
          v-for="(history, index) in searchHistory"
          @click:close="removeSearchHistory(history.id)"
          @click="onSearchHistory"
        >
          {{ history.search_term }}
        </v-chip>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import { mapActions, mapState } from "vuex";
export default {
  data() {
    return {
      searchTerm: ""
    };
  },
  computed: {
    ...mapState({
      sites: state => state.bookmark.bookmark.sites,
      locked: state => state.bookmark.bookmark.locked,
      searchHistory: state => state.search.searchHistory
    })
  },
  methods: {
    ...mapActions("search", ["removeSearchHistory"]),
    openSearch() {
      for (let i = 0; i < this.sites.length; i++) {
        if (this.sites[i].name === this.locked) {
          window.open(`${this.sites[i].site_url}${this.searchTerm}`);
        }
      }
    },
    onSearch() {
      this.$store.dispatch("search/createSearchHistory", this.searchTerm);
      this.openSearch();
    },
    onSearchHistory(event) {
      this.searchTerm = event.target.innerText;
      this.openSearch();
    }
  }
};
</script>
