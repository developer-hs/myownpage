<template>
  <div id="app" class="app">
    <div class="container">
      <figure class="content">
        <figcaption class="title">Rotation box</figcaption>
        <div id="red-box"></div>
      </figure>

      <figure class="content">
        <figcaption class="title">Animating boxes</figcaption>
        <div class="box-wrapper">
          <div ref="box1" class="box" />
          <div ref="box2" class="box" />
          <div ref="box3" class="box" />
          <div ref="box4" class="box" />
          <div ref="box5" class="box" />
          <div ref="box6" class="box" />
          <div ref="box7" class="box" />
          <div ref="box8" class="box" />
          <div ref="box9" class="box" />
          <div ref="box10" class="box" />
        </div>
      </figure>
    </div>
  </div>
</template>

<script>
import { gsap } from "gsap";

export default {
  name: "App",
  mounted() {
    const tl = gsap.timeline({
      repeat: -1
    });
    tl.to("#red-box", {
      x: 500,
      y: 50,
      duration: 3,
      rotation: 720
    }).to("#red-box", {
      x: 0,
      y: 0,
      duration: 2,
      rotation: -720
    });

    const tl3 = gsap.timeline({
      repeat: -1,
      yoyo: true
    });

    for (const key in this.$refs) {
      tl3.to(this.$refs[key], {
        delay: -0.1,
        ease: "elastic.out(0.1, 0.5)",
        y: 100
      });
    }
    for (const key in this.$refs) {
      tl3.to(this.$refs[key], {
        rotation: 200,
        scale: 0.5,
        backgroundColor: "#72b165",
        delay: -0.2
      });
    }
  }
};
</script>

<style scoped>
html,
body,
.app {
  margin: 0;
  padding: 0;
}
.app {
  display: flex;
  width: 100%;
  height: 100vh;
  background: lightyellow;
}

.container {
  flex: 1;
  flex-direction: column;
  justify-content: space-between;
}

.content {
  position: relative;
  width: 100%;
}

.content .title {
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.content + .content {
  margin-top: 96px;
}

.card {
  position: relative;
}

.card .card-inner {
  position: absolute;
  height: 8rem;
  width: 8rem;
  margin-left: 0;
  margin-top: 0;
  background-color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
}

.card .card-shadow {
  position: absolute;
  height: 8rem;
  width: 8rem;
  margin-left: 0.25rem;
  margin-top: 0.25rem;
  background-color: lightseagreen;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 0;
}

.box {
  padding: 0.25rem;
  background: lightgreen;
  width: 3rem;
  height: 3rem;
  margin-right: 0.25rem;
}

#red-box {
  width: 3rem;
  height: 2.5rem;
  background-color: lightcoral;
  border-bottom: 8px solid darkgreen;
  border-radius: 4px;
  padding: 0.5rem;
  margin-bottom: 0.125rem;
}

.box-wrapper {
  display: flex;
}
</style>
