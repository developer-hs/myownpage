export const DateConversion = {
  methods: {
    monthConversion(month) {
      if (String(month).length === 1) {
        return `0${month + 1}`;
      } else {
        return month;
      }
    },
    dateConversion(date) {
      if (String(date).length === 1) {
        return `0${date}`;
      } else return date;
    },
    hoursConversion(hours) {
      if (String(hours).length === 1) {
        return `0${hours}`;
      } else return hours;
    },
    minuteConversion(minute) {
      if (String(minute).length === 1) {
        return `0${minute}`;
      } else return minute;
    },
  },
};
