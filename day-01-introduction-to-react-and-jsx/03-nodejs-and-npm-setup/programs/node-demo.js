/**
 * Practical: Node.js Runtime Demonstration
 * 
 * Run this program from your terminal:
 *   node node-demo.js
 * 
 * This proves that JavaScript executes directly on your machine through the
 * V8 engine in Node.js, outside of any web browser.
 */

console.log("==================================================");
console.log("🎓 Node.js Runtime Verification");
console.log("==================================================");

// 1. System & Runtime Information
console.log(`Node.js Version : ${process.version}`);
console.log(`Platform / OS   : ${process.platform} (${process.arch})`);
console.log(`Current Dir     : ${process.cwd()}`);
console.log("--------------------------------------------------");

// 2. Data Processing (College Student Grade Evaluation)
const students = [
  { rollNo: "CS-101", name: "Ananya", marks: [85, 90, 78, 92] },
  { rollNo: "CS-102", name: "Bala", marks: [65, 70, 58, 62] },
  { rollNo: "CS-103", name: "Deepak", marks: [95, 88, 91, 89] }
];

console.log("Calculating Student Averages:");
students.forEach(student => {
  const total = student.marks.reduce((sum, m) => sum + m, 0);
  const avg = (total / student.marks.length).toFixed(2);
  const status = avg >= 75 ? "Distinction" : "First Class";
  console.log(`- [${student.rollNo}] ${student.name.padEnd(8)} | Avg: ${avg}% | Result: ${status}`);
});

console.log("==================================================");
console.log("✅ Node.js successfully executed JavaScript locally!");
