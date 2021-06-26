<template>
  <svg
    version="1.0"
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 211.000000 129.000000"
    preserveAspectRatio="xMidYMid meet"
  >
    <g
      transform="translate(0.000000,129.000000) scale(0.100000,-0.100000)"
      fill="#000000"
      stroke="none"
    >
      <path
        d="M966 1279 c-107 -15 -229 -87 -275 -163 -13 -21 -41 -44 -74 -60
-127 -62 -198 -167 -198 -291 0 -276 353 -426 606 -256 l31 20 44 -29 c189
-125 465 -59 560 134 53 107 40 224 -37 324 -32 42 -134 109 -179 118 -24 4
-40 16 -55 40 -72 116 -254 187 -423 163z"
      />
      <path
        class="rainDropOne"
        d="M560 400 c0 -13 7 -20 20 -20 13 0 20 7 20 20 0 13 -7 20 -20 20 -13
0 -20 -7 -20 -20z"
      />
      <path
        class="rainDropTwo"
        d="M1520 400 c0 -13 7 -20 20 -20 13 0 20 7 20 20 0 13 -7 20 -20 20
-13 0 -20 -7 -20 -20z"
      />
      <path
        class="rainDropThree"
        d="M1040 330 c0 -13 7 -20 20 -20 13 0 20 7 20 20 0 13 -7 20 -20 20
-13 0 -20 -7 -20 -20z"
      />
      <path
        class="rainDropFour"
        d="M780 290 c0 -13 7 -20 20 -20 13 0 20 7 20 20 0 13 -7 20 -20 20 -13
0 -20 -7 -20 -20z"
      />
      <path
        class="rainDropFive"
        d="M1300 290 c0 -13 7 -20 20 -20 13 0 20 7 20 20 0 13 -7 20 -20 20
-13 0 -20 -7 -20 -20z"
      />
    </g>
  </svg>
</template>
<script>
import gsap from "gsap";

export default {
  mounted() {
    let tl = gsap.timeline();

    tl.from(".rainDropOne", {
      repeat: -1,
      y: -100,
      ease: "none",
      duration: 0.6
    });

    tl.from(".rainDropTwo", {
      repeat: -1,
      y: -100,
      ease: "none",
      duration: 0.7
    });

    tl.from(".rainDropThree", {
      repeat: -1,
      y: -60,
      ease: "none",
      duration: 1
    });

    tl.from(".rainDropFour", {
      repeat: -1,
      y: -55,
      ease: "none",
      duration: 0.5
    });
    tl.from(".rainDropFive", {
      repeat: -1,
      y: -55,
      ease: "none",
      duration: 0.5
    });
  }
};
</script>

<style scoped>
.svg {
  width: 15%;
  margin: 0 auto;
  display: block;
  margin-top: 4%;
}
</style>
