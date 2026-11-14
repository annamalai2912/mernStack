// Run with: node node-demo.js
console.log("Hello! Node.js is running JavaScript on your computer.");

const student = "Alex";
const marks = [80, 90, 85];
const average = marks.reduce((a, b) => a + b, 0) / marks.length;

console.log(`Student: ${student}`);
console.log(`Average: ${average}%`);
