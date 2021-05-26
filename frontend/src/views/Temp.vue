<template>
  <div>
    <h1>Welcome to {{ title2 }}!</h1>
    <input type="text" v-model="input1" />
    <button type="button" @click="getData">Get</button>
    <button type="button" @click="setData">Set</button>
    <button type="button" @click="tableToggle">Toggle</button>
    <select class="select-form" v-model="region" @change="changeRegion">
      <option :key="i" :value="d.v" v-for="(d, i) in options">{{ d.t }}</option>
    </select>
    <v-simple-table v-show="tableShow">
      <template v-slot:default>
        <thead>
          <tr :key="i" v-for="(d, i) in options">
            <td class="text-left">
              {{ d.t }}
            </td>
            <td class="text-left">
              {{ d.v }}
            </td>
          </tr>
        </thead>
      </template>
    </v-simple-table>
    <v-container fluid>
      <v-row align="center">
        <v-col class="d-flex" cols="12" sm="6">
          <v-select :items="items" label="Standard"></v-select>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
import { mapGetters, mapMutations, mapState, mapActions } from "vuex";
export default {
  data: () => ({
    title: "Vue js",
    title2: "Seoul",
    input1: "abcd",
    options: [
      { v: "S", t: "Seoul" },
      { v: "J", t: "Jeju" },
      { v: "B", t: "Busan" },
    ],
    region: "B",
    items: ["Foo", "Bar", "Fizz", "Buzz"],
    tableShow: true,
  }),
  computed: {
    ...mapGetters({
      change1: "function1",
      change2: "function2 ",
    }),
    // ...mapGetters(["function1", "function2"]),
    ...mapState(["state_key"]),
  },
  watch: {
    input() {
      console.log(this.input1);
    },
  },

  methods: {
    ...mapMutations(["funtion1"]),
    ...mapActions(["action1", "action2"]),
    // setState() {
    //   this.action1(attribute)
    // },
    getData() {
      alert(this.input1);
    },
    setData() {
      this.input1 = "12345";
    },
    changeRegion() {
      alert(this.region);
    },
    tableToggle() {
      this.tableShow = !this.tableShow;
    },
  },
  beforeCreate() {
    console.log("beforeCreate");
  },
  created() {
    console.log("created");
  },
  beforeMount() {
    console.log("beforeMount");
  },
  mounted() {
    console.log("mounted");
  },
  beforeUpdate() {
    console.log("beforeUpdate");
  },
  updated() {
    console.log("updated");
  },
  beforeDestroy() {
    console.log("beforeDestroy");
  },
  destroyed() {
    console.log("destroyed");
  },
};
</script>

<style scoped>
.select-form {
  border: 1px solid;
  width: 20rem;
  align-content: center;
  display: flex;
  justify-content: center;
  text-align: center;
}
</style>
