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
      console.log(date);
      if (String(date).length === 1) {
        return `0${date}`;
      } else return date;
    },
  },
};
