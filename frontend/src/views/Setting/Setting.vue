<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      fullscreen
      hide-overlay
      transition="dialog-bottom-transition"
    >
      <v-card>
        <v-toolbar dark color="primary">
          <v-btn icon dark @click="dialogToggle(false)">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title>Settings</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <bookmark-setting />
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>
import { mapGetters, mapMutations } from "vuex";
import BookmarkSetting from "./BookmarkSetting.vue";
export default {
  components: {
    BookmarkSetting
  },
  data() {
    return {
      notifications: false,
      sound: true,
      widgets: false
    };
  },
  computed: {
    ...mapGetters("settings", { dialog: "settingDialog" })
  },
  methods: {
    ...mapMutations("settings", ["dialogToggle"])
  }
};
</script>
