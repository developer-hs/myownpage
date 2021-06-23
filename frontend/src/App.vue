<template>
  <div id="app">
    <v-app id="inspire">
      <v-main>
        <router-view></router-view>
      </v-main>
      <v-footer color="black" app>
        <span class="white--text">&copy; {{ new Date().getFullYear() }}</span>
      </v-footer>
    </v-app>
  </div>
</template>

<script>
export default {
  data: () => ({})
};
</script>

<style></style>
