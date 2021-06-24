<template>
  <v-container id="a">
    <svg id="a">
      <path
        d="M 2.5,0 C 2.6949458,3.5392017 3.344765,20.524571 4.4494577,30.9559 5.7551357,42.666753 4.5915685,50 2.5,50 0.40843152,50 -0.75513565,42.666753 0.55054234,30.9559 1.655235,20.524571 2.3050542,3.5392017 2.5,0 Z"
      />
    </svg>
  </v-container>
</template>
<script>
export default {
  mounted() {
    let svg = document.createElementNS("SVG", "path");
    const droplets = 250;
    for (let r = 0; r < droplets; r++) {
      svg.setAttribute(
        "d",
        "M 2.5,0 C 2.6949458,3.5392017 3.344765,20.524571 4.4494577,30.9559 5.7551357,42.666753 4.5915685,50 2.5,50 0.40843152,50 -0.75513565,42.666753 0.55054234,30.9559 1.655235,20.524571 2.3050542,3.5392017 2.5,0 Z"
      );
      svg.setAttribute("x", `${Math.floor(Math.random() * 100)}`);
      svg.setAttribute("y", `${Math.floor(Math.random() * 100)}`);
      svg.setAttribute("o", `${Math.random()}`);
      svg.setAttribute("a", `${Math.random() + 0.5}`);
      svg.setAttribute("s", `${Math.random()}`);
      svg.setAttribute("strok", "none");
      svg.setAttribute("viewBox", "0 0 5 50");
      svg.setAttribute("heigth", "30px");
      svg.id = "rain";
      console.log(svg);
      document.querySelector("#a").appendChild(svg);
    }
  }
};
</script>
<style scoped>
#rain {
  height: 30px;
  position: absolute;
}
</style>
