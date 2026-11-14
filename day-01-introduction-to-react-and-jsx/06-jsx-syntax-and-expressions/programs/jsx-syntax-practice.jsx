// Practical: Practicing JSX Syntax and Dynamic Expressions
export default function JsxSyntaxPractice() {
  const studentName = "Priya";
  const department = "Computer Science";
  const attendance = 85;

  return (
    <div style={{ fontFamily: 'sans-serif', padding: '20px' }}>
      <h2>Student Profile</h2>
      <p>Name: {studentName}</p>
      <p>Department: {department}</p>
      <p>Attendance: {attendance}%</p>
      <p>Exam Eligibility: {attendance >= 75 ? "Eligible" : "Shortage"}</p>
    </div>
  );
}
