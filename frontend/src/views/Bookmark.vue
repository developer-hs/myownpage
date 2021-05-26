<template>
  <v-flex>
    <div class="text-xs-center justify-center">
      <v-btn
        fab
        depressed
        class="mr-3 font-weight-medium"
        color="white"
        small
        :key="i"
        v-for="(d, i) in userInfo.bookmark.sites"
        @click="SelectSite"
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
      site: "NAVER",
    };
  },
  computed: {
    ...mapState({
      userInfo: (state) => state.auth.userInfo,
    }),
  },
  methods: {
    SelectSite() {},
  },
};
</script>
