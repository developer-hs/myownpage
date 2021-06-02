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
          overflow
          app
        >
          <v-divider></v-divider>

          <v-list dense nav>
            <v-list-item v-for="menu in settingsMenu" :key="menu.title" link>
              <v-list-item-icon>
                <v-icon>{{ menu.icon }}</v-icon>
              </v-list-item-icon>

              <v-list-item-content @click="selectMenu = menu.title">
                <v-list-item-title>{{ menu.title }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
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
        <main-setting v-if="selectMenu === 'Main Setting'" />
        <bookmark-setting v-if="selectMenu === 'Bookmark Setting'" />
      </v-app>
    </v-app>
  </div>
</template>
<script>
import { mapState } from "vuex";
import BookmarkSetting from "../views/Setting/BookmarkSetting.vue";
import MainSetting from "../views/Setting/MainSetting.vue";
export default {
  components: { MainSetting, BookmarkSetting },
  data() {
    return {
      selectMenu: "Bookmark Setting",
      settingsMenu: [
        { title: "Main Setting", icon: "mdi-view-dashboard" },
        { title: "Bookmark Setting", icon: "mdi-image" },
        { title: "About", icon: "mdi-help-box" },
      ],
      right: null,
    };
  },
  computed: {
    ...mapState({
      footer: (state) => state.settings.footer,
      primaryDrawer: (state) => state.settings.primaryDrawer,
    }),
  },
  methods: {
    toggleSetting(event) {
      const elementText = event.target.innerText;
      console.log(elementText.split(" "));
    },
  },
};
</script>
