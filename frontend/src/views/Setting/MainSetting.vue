<template>
  <v-main>
    <v-container fluid>
      <v-row align="center" justify="center">
        <v-col cols="10">
          <v-card>
            <v-card-text>
              <v-row>
                <v-col cols="12" md="6">
                  <span>Scheme</span>
                  <v-switch
                    v-model="$vuetify.theme.dark"
                    primary
                    label="Dark"
                  ></v-switch>
                </v-col>
                <v-col cols="12" md="6">
                  <span>Drawer</span>
                  <v-radio-group v-model="primaryDrawer.type" column>
                    <v-radio
                      v-for="drawer in drawers"
                      :key="drawer"
                      :label="drawer"
                      :value="drawer.toLowerCase()"
                      primary
                    ></v-radio>
                  </v-radio-group>
                  <v-switch
                    v-model="primaryDrawer.clipped"
                    label="Clipped"
                    primary
                  ></v-switch>
                  <v-switch
                    v-model="primaryDrawer.floating"
                    label="Floating"
                    primary
                  ></v-switch>
                  <v-switch
                    v-model="primaryDrawer.mini"
                    label="Mini"
                    primary
                  ></v-switch>
                </v-col>
                <v-col cols="12" md="6">
                  <span>Footer</span>
                  <v-switch
                    v-model="footer.inset"
                    label="Inset"
                    primary
                  ></v-switch>
                </v-col>
              </v-row>
            </v-card-text>
            <v-card-actions>
              <v-btn color="red" text @click="logOut">LogOut</v-btn>

              <v-spacer></v-spacer>
              <v-btn text @click="$router.push({name : 'home'})">Cancel</v-btn>
              <v-btn text color="primary">Submit</v-btn>
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
      drawers: (state) => state.settings.drawers,
      primaryDrawer: (state) => state.settings.primaryDrawer,
    }),
  },
  methods: {
    ...mapActions("auth", ["logOut"]),
  },
};
</script>
