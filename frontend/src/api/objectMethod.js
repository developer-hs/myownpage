export const findObjectIndex = (objects, targetId) => {
  for (let i = 0; i < objects.length; i++) {
    if (objects[i].id === targetId) {
      return i;
    }
  }
};
