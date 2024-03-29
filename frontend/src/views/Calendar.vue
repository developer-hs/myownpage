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
          class="rounded-lg"
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
              <span v-html="selectedEvent.detail"></span>
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
    <!-- !스케줄 등록 DIALOG -->
    <v-dialog v-model="dialog" max-width="70rem">
      <v-card class="pa-6">
        <v-card-text>
          <v-row>
            <v-col cols="12" sm="6">
              <!-- 일정 등록 form -->
              <v-text-field
                v-model="calendarObj.name"
                label="일정"
                prepend-icon="mdi-pencil"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <!-- 날짜 지정 form -->
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
                    label="날짜"
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
              <!-- 시간 설정 form -->
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
                    :disabled="!timed"
                    v-model="calendarObj.time"
                    label="시간"
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
            <!-- 시간설정여부 확인 form -->
            <v-col>
              <v-checkbox
                v-model="calendarObj.timed"
                :label="'시간설정'"
              ></v-checkbox>
            </v-col>
            <!-- 색상 form -->
            <v-col>
              <v-text-field
                prepend-icon="mdi-palette"
                v-model="calendarObj.color"
                hide-details
                class="ma-0 pa-0"
              >
                <template v-slot:append>
                  <v-menu
                    v-model="menu"
                    top
                    nudge-bottom="105"
                    nudge-left="16"
                    :close-on-content-click="false"
                  >
                    <template v-slot:activator="{ on }">
                      <div :style="swatchStyle" v-on="on" />
                    </template>
                    <v-card flat>
                      <v-card-text class="pa-0">
                        <v-color-picker v-model="calendarObj.color" flat />
                      </v-card-text>
                    </v-card>
                  </v-menu>
                </template>
              </v-text-field>
            </v-col>
          </v-row>
        </v-card-text>
        <!-- !상세일정 -->
        <tip-tap-component
          :EditorContent="EditorContent"
          @changeContent="setContent"
          class="pl-6 pr-5"
        />
        <v-row justify="end">
          <v-btn text @click="dialog = false">
            Cancel
          </v-btn>
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
import { DateConversion } from "./mixins/DateConversion";
import { findObjectIndex } from "../api/objectMethod";
import TipTapComponent from "./partial/TipTapComponent.vue";

export default {
  mixins: [DateConversion],
  components: { TipTapComponent },
  data() {
    return {
      // calendar schedule form data
      calendarObj: {
        name: "",
        dates: [],
        time: "",
        color: "#BCAAA4",
        timed: false,
        detail: ""
      },
      updateMode: false,
      timeMenu: false,
      dateMenu: false,
      dialog: false,

      detailFor: 1,
      newDate: "",
      focus: "",
      type: "month",

      selectedEvent: {},
      selectedElement: null,
      selectedOpen: false,
      menu: false,
      EditorContent: ""
    };
  },

  computed: {
    ...mapState({
      schedule: state => state.calendar.schedule
    }),
    timed() {
      return this.calendarObj.timed;
    },
    dateRangeText() {
      return this.calendarObj.dates.join(" ~ ");
    },
    nowDate() {
      return this.$refs.calendar.title;
    },
    // color picker
    swatchStyle() {
      const color = this.calendarObj.color;
      const menu = this.menu;
      return {
        backgroundColor: color,
        cursor: "pointer",
        height: "30px",
        width: "30px",
        borderRadius: menu ? "50%" : "4px",
        transition: "border-radius 200ms ease-in-out"
      };
    }
  },
  mounted() {
    this.$refs.calendar.checkChange();
  },
  watch: {
    dialog(val) {
      if (val === false) {
        this.EditorContent = "";
      }
    }
  },
  methods: {
    setContent(content) {
      // tiptap 에서 전달받은 content 를 update / create form 에 옮김
      this.calendarObj.detail = content;
    },
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
      const index = findObjectIndex(this.schedule, schedule.id);
      schedule = this.schedule[index];

      this.calendarObjInit();
      this.updateMode = true;
      const startYear = schedule.start.getFullYear();
      const startMonth = this.monthConversion(schedule.start.getMonth());
      const startDate = this.dateConversion(schedule.start.getDate());
      const endYear = schedule.end.getFullYear();
      const endMonth = this.monthConversion(schedule.end.getMonth());
      const endDate = this.dateConversion(schedule.end.getDate());

      const hours = this.hoursConversion(schedule.start.getHours());
      const minute = this.minuteConversion(schedule.start.getMinutes());

      const fullStartDay = `${startYear}-${startMonth}-${startDate}`;
      const fullEndDay = `${endYear}-${endMonth}-${endDate}`;
      const fullTime = `${hours}:${minute}`;

      this.calendarObj.dates = [fullStartDay, fullEndDay];
      this.calendarObj.time = fullTime;
      this.calendarObj.timed = schedule.timed;
      this.calendarObj.name = schedule.name;
      this.calendarObj.color = schedule.color;
      this.calendarObj.id = schedule.id;
      // EditorContent : tiptap 정의된 룰에 따라 update 하기위해 props 값 설정
      this.EditorContent = schedule.detail;
    },
    calendarObjInit() {
      this.calendarObj.name = "";
      this.calendarObj.dates = [];
      this.calendarObj.time = "";
      this.calendarObj.color = "#BCAAA4";
      this.calendarObj.timed = true;
      this.calendarObj.detail = "";
      this.detailFor = 1;
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
    }
  }
};
</script>
