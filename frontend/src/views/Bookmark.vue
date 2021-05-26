<template>
  <v-flex>
    <v-btn class="mr-3" :key="i" v-for="(d, i) in userInfo.bookmark.sites">
      {{ d.name }}
    </v-btn>
  </v-flex>
</template>
<script>
import { mapState } from "vuex";

export default {
  data() {
    return {};
  },
  computed: {
    ...mapState("auth", ["userInfo"]),
  },
};
</script>
