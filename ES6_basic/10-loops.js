export default function appendToEachArrayValue(array, appendString) {
  const newArray = [];
  for (let element of array) {
    const value = element;
    element = appendString + value;
    newArray.push(element);
  }
  return newArray;
}
