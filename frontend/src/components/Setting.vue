<template>
  <div id="app">
    <v-app id="inspire">
      <v-app id="sandbox">
        <v-navigation-drawer
          v-model="primaryDrawer.model"
          :clipped="primaryDrawer.clipped"
          :floating="primaryDrawer.floating"
          :mini-variant="primaryDrawer.mini"
          :permanent="primaryDrawer.type === 'permanent'"
          :temporary="primaryDrawer.type === 'temporary'"
          app
          overflow
        >
          <v-col class="text-center">BookMark Settings</v-col>
        </v-navigation-drawer>

        <v-app-bar :clipped-left="primaryDrawer.clipped" app>
          <v-app-bar-nav-icon
            v-if="primaryDrawer.type !== 'permanent'"
            @click.stop="primaryDrawer.model = !primaryDrawer.model"
          ></v-app-bar-nav-icon>
          <v-toolbar-title>Vuetify</v-toolbar-title>
        </v-app-bar>

        <v-footer :inset="footer.inset" app>
          <span class="px-4">&copy; {{ new Date().getFullYear() }}</span>
        </v-footer>
        <main-setting :primaryDrawer="primaryDrawer" />
      </v-app>
    </v-app>
  </div>
</template>
<script>
import { mapState } from "vuex";
import MainSetting from "../views/Setting/MainSetting.vue";
export default {
  components: { MainSetting },
  data() {
    return {};
  },
  computed: {
    ...mapState({
      footer: (state) => state.settings.footer,
      primaryDrawer: (state) => state.settings.primaryDrawer,
    }),
  },
};
</script>
