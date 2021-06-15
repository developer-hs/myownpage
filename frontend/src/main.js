import vuetify from "./plugins/vuetify";
import Vue from "vue";
import App from "./App.vue";
import store from "./store";
import router from "./router";

Vue.config.productionTip = false;
export const eventBus = new Vue();

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
