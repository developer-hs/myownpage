<template>
  <div>
    <!-- <HeaderVue /> -->
    <div id="content" class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
// import HeaderVue from "./components/layout/Header.vue";

export default {
  data: function() {
    return {
      name: "cslee",
    };
  },
  components: {
    // HeaderVue,
  },
};
</script>

<style></style>
