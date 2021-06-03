<template>
  <v-row class="fill-height">
    <v-col>
      <v-sheet height="64">
        <v-toolbar flat>
          <v-btn outlined class="mr-4" color="grey darken-2" @click="setToday">
            Today
          </v-btn>
          <v-btn fab text small color="grey darken-2" @click="prev">
            <v-icon small>
              mdi-chevron-left
            </v-icon>
          </v-btn>
          <v-btn fab text small color="grey darken-2" @click="next">
            <v-icon small>
              mdi-chevron-right
            </v-icon>
          </v-btn>
          <v-toolbar-title v-if="$refs.calendar">
            {{ $refs.calendar.title }}
          </v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
      </v-sheet>
      <v-sheet height="600">
        <v-calendar
          ref="calendar"
          v-model="focus"
          color="primary"
          :events="schedule"
          :event-color="getEventColor"
          :type="type"
          @click:event="showEvent"
          @click:more="viewDay"
          @click:date="viewDay"
          @change="$store.dispatch('calendar/getSchedule')"
        ></v-calendar>
        <v-menu
          v-model="selectedOpen"
          :close-on-content-click="false"
          :activator="selectedElement"
          offset-x
        >
          <v-card color="grey lighten-4" min-width="350px" flat>
            <v-toolbar :color="selectedEvent.color" dark>
              <v-btn
                icon
                @click="
                  dialog = true;
                  updateDataInit(selectedEvent);
                "
              >
                <v-icon>mdi-pencil</v-icon>
              </v-btn>
              <v-toolbar-title v-html="selectedEvent.name"></v-toolbar-title>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon>mdi-heart</v-icon>
              </v-btn>
              <v-btn icon>
                <v-icon>mdi-dots-vertical</v-icon>
              </v-btn>
            </v-toolbar>
            <v-card-text>
              <span v-html="selectedEvent.details"></span>
            </v-card-text>
            <v-card-actions>
              <v-btn
                text
                color="red"
                @click="
                  selectedOpen = false;
                  deleteSchedule(selectedEvent.id);
                "
              >
                Delete
              </v-btn>
              <v-btn text color="secondary" @click="selectedOpen = false">
                Cancel
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-menu>
      </v-sheet>
    </v-col>
    <!-- 스케줄 등록 DIALOG -->
    <v-dialog v-model="dialog" max-width="70rem">
      <v-card class="pa-6">
        <v-card-text>
          <v-row>
            <v-col cols="12" sm="6">
              <v-text-field
                v-model="calendarObj.name"
                label="일정"
                prepend-icon="mdi-pencil"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" sm="6">
              <v-menu
                ref="menu"
                v-model="dateMenu"
                :close-on-content-click="false"
                :nudge-right="40"
                :return-value.sync="calendarObj.time"
                transition="scale-transition"
                offset-y
                max-width="290px"
                min-width="290px"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="dateRangeText"
                    label="Date Range"
                    prepend-icon="mdi-calendar-month-outline"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="calendarObj.dates"
                  range
                  elevation="15"
                ></v-date-picker>
              </v-menu>
            </v-col>
            <v-col cols="12" sm="6">
              <v-menu
                ref="menu"
                v-model="timeMenu"
                :close-on-content-click="false"
                :nudge-right="40"
                :return-value.sync="calendarObj.time"
                transition="scale-transition"
                offset-y
                max-width="290px"
                min-width="290px"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="calendarObj.time"
                    label="Picker in menu"
                    prepend-icon="mdi-clock-time-four-outline"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-time-picker
                  v-if="timeMenu"
                  v-model="calendarObj.time"
                  full-width
                  @click:minute="$refs.menu.save(calendarObj.time)"
                ></v-time-picker>
              </v-menu>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-checkbox
                v-model="calendarObj.timed"
                :label="'시간설정'"
              ></v-checkbox>
            </v-col>
            <v-col>
              <v-select
                :items="colors"
                v-model="calendarObj.color"
                label="Colors"
                prepend-icon="mdi-palette"
              ></v-select>
            </v-col>
          </v-row>
        </v-card-text>
        <v-row justify="end">
          <v-btn
            v-if="!updateMode"
            text
            color="primary"
            @click="
              dialog = false;
              createSchedule();
            "
          >
            Submit
          </v-btn>
          <v-btn
            v-else
            text
            color="primary"
            @click="
              dialog = false;
              updateSchedule();
            "
          >
            Update
          </v-btn>
        </v-row>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>
import { mapState } from "vuex";

export default {
  data() {
    return {
      // calendar schedule form data
      calendarObj: {
        name: "",
        dates: [],
        time: null,
        color: "blue",
        timed: true,
      },
      updateMode: false,
      timeMenu: false,
      dateMenu: false,

      newDate: "",
      dialog: false,
      focus: "",
      type: "month",
      typeToLabel: {
        month: "Month",
        week: "Week",
        day: "Day",
        "4day": "4 Days",
      },
      selectedEvent: {},
      selectedElement: null,
      selectedOpen: false,
      colors: [
        "blue",
        "indigo",
        "deep-purple",
        "cyan",
        "green",
        "orange",
        "grey darken-1",
      ],
      names: [
        "Meeting",
        "Holiday",
        "PTO",
        "Travel",
        "Event",
        "Birthday",
        "Conference",
        "Party",
      ],
    };
  },

  computed: {
    ...mapState({
      schedule: (state) => state.calendar.schedule,
    }),
    dateRangeText() {
      console.log("dateRangeText");
      console.log(this.calendarObj.dates);

      return this.calendarObj.dates.join(" ~ ");
    },
    nowDate() {
      return this.$refs.calendar.title;
    },
  },
  mounted() {
    this.$refs.calendar.checkChange();
  },
  methods: {
    createSchedule() {
      if (this.calendarObj.dates.length == 1) {
        this.calendarObj.dates.push(this.calendarObj.dates[0]);
      }
      this.$store.dispatch("calendar/createSchedule", this.calendarObj);
    },
    deleteSchedule(pk) {
      this.$store.dispatch("calendar/deleteSchedule", pk);
    },
    updateSchedule() {
      this.$store.dispatch("calendar/updateSchedule", this.calendarObj);
    },
    updateDataInit(schedule) {
      this.calendarObjInit();
      this.updateMode = true;
      const startDate = schedule.start.split(" ");
      const startDay = startDate[0];
      const time = startDate[1];
      const endDay = schedule.end.split(" ")[0];
      this.calendarObj.dates = [startDay, endDay];
      this.calendarObj.time = time;
      this.calendarObj.name = schedule.name;
      this.calendarObj.color = schedule.color;
      this.calendarObj.id = schedule.id;
    },
    calendarObjInit() {
      this.calendarObj.name = "";
      this.calendarObj.dates = [];
      this.calendarObj.time = null;
      this.calendarObj.color = "blue";
      this.calendarObj.timed = true;
    },
    // 날짜 클릭시 호출
    viewDay({ date }) {
      this.updateMode = false;
      this.dialog = !this.dialog;
      this.focus = date;
      this.calendarObjInit();
      this.calendarObj.dates.push(date);
    },
    getEventColor(event) {
      return event.color;
    },
    setToday() {
      this.focus = "";
    },
    prev() {
      this.$refs.calendar.prev();
    },
    next() {
      this.$refs.calendar.next();
    },
    showEvent({ nativeEvent, event }) {
      const open = () => {
        this.selectedEvent = event;
        this.selectedElement = nativeEvent.target;
        requestAnimationFrame(() =>
          requestAnimationFrame(() => (this.selectedOpen = true))
        );
      };

      if (this.selectedOpen) {
        this.selectedOpen = false;
        requestAnimationFrame(() => requestAnimationFrame(() => open()));
      } else {
        open();
      }

      nativeEvent.stopPropagation();
    },

    rnd(a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a;
    },
  },
};
</script>
