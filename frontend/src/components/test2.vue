<template>
  <v-container style="height:1000px" id="rain">
    <svg
      id="rain_drop"
      viewBox="0 0 5 50"
      preserveAspectRatio="xMinYMin"
      style="--x: 34; --y: 79; --o: 0.5751990119468688; --a: 0.6662096332771401; --d: -0.5105620553615169; --s: 0.645979367880021"
    >
      <path
        d="M 2.5,0 C 2.6949458,3.5392017 3.344765,20.524571 4.4494577,30.9559 5.7551357,42.666753 4.5915685,50 2.5,50 0.40843152,50 -0.75513565,42.666753 0.55054234,30.9559 1.655235,20.524571 2.3050542,3.5392017 2.5,0 Z"
      ></path>
    </svg>
  </v-container>
</template>
<script>
export default {
  mounted() {
    const droplets = 250;
    for (let i = 0; i < droplets; i++) {
      const rainSVG = document.createElement("svg");
      const rain = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "path"
      );
      rain.setAttribute(
        "d",
        "M 2.5,0 C 2.6949458,3.5392017 3.344765,20.524571 4.4494577,30.9559 5.7551357,42.666753 4.5915685,50 2.5,50 0.40843152,50 -0.75513565,42.666753 0.55054234,30.9559 1.655235,20.524571 2.3050542,3.5392017 2.5,0 Z"
      );
      rainSVG.setAttribute("viewBox", "0 0 5 50");
      rainSVG.setAttribute("preserveAspectRatio", "xMinYMin");
      rainSVG.id = "rain_drop";
      rainSVG.setAttribute(
        "style",
        `--x:${Math.floor(Math.random() * 100)}; --y: ${Math.floor(
          Math.random() * 100
        )}; --o: ${Math.random()}; --a :${Math.random() +
          0.5}; --s: ${Math.random()};`
      );

      rainSVG.appendChild(rain);
      const doc = document.querySelector("#rain");
      doc.appendChild(rainSVG);
    }
  }
};
</script>
<style scoped>
* *:before *:after {
  box-sizing: border-box;
}

body {
  background-color: white;
  display: flex;
  align-items: center;
  justify-content: center;
}
#rain__drop {
  animation-delay: calc(var(--d) * 1s);
  animation-duration: calc(var(--a) * 1s);
  animation-iteration-count: infinite;
  animation-name: drop;
  animation-timing-function: linear;
  height: 30px;
  left: calc(var(--x) * 1%);
  position: absolute;
  top: calc((var(--y) + 50) * -1px);
}
#rain_drop path {
  fill: #a1c6cc;
  opacity: var(--o);
  transform: scaleY(calc(var(--s) * 1.5));
}
@keyframes drop {
  90% {
    opacity: 1;
  }
  100% {
    opacity: 0;
    transform: translateY(100vh);
  }
}
</style>
