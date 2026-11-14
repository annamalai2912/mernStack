// Exercise: Fix the JSX syntax errors in this component
export default function StudentReport() {
  const student = "Rahul";
  const marks = 85;

  return (
    // Hint: Use className instead of class, close all tags, and wrap in a single parent
    <div className="card">
      <h3>Student: {student}</h3>
      <p>Score: {marks} / 100</p>
      <p>Result: {marks >= 50 ? "Passed" : "Failed"}</p>
      <input type="text" placeholder="Teacher comments" />
    </div>
  );
}
