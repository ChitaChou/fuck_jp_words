export const name2title = name => {
  // check if any lower case letter followed by upper case letter
  // HelloRealtimeNLP => Hello Realtime NLP
  return name.replace(/([a-z](?=[A-Z]))/g, "$1 ");
};