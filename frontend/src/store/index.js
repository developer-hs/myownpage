import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

import auth from "./auth";
import notepads from "./notepads";
import bookmark from "./bookmark";
import search from "./search";
import settings from "./settings";
export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: { auth, notepads, bookmark, search, settings },
});
