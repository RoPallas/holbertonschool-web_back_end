import ClassRoom from './0-classroom';

function initializeRooms() {
  const salon1 = new ClassRoom(19);
  const salon2 = new ClassRoom(20);
  const salon3 = new ClassRoom(34);
  const listaSalones = [salon1, salon2, salon3];
  return listaSalones;
}

module.exports = initializeRooms;
