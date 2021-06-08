<template>
  <v-main>
    <v-container fluid>
      <v-row align="center" justify="center">
        <v-col cols="10">
          <v-card>
            <v-card-text>
              <v-row>
                <v-col cols="12" md="6">
                  <span>Sites</span>
                  <v-switch
                    v-for="site in Object.keys(sites)"
                    :key="site"
                    :label="site"
                    v-model="sites[site]"
                    primary
                  ></v-switch>
                </v-col>
                <v-col cols="12" md="6"> </v-col>
                <v-col cols="12" md="6"> </v-col>
              </v-row>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn text @click="$router.push({name:'home'})">Cancel</v-btn>
              <v-btn
                @click="$store.dispatch('settings/bookmarkSetting')"
                text
                color="primary"
                >Submit</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  data() {
    return {};
  },
  computed: {
    ...mapState({
      footer: (state) => state.settings.footer,
      sites: (state) => state.settings.sites,
      primaryDrawer: (state) => state.settings.primaryDrawer,
    }),
  },
  methods: {
    ...mapActions("auth", ["logOut"]),
  },
};
</script>
