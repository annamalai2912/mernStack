// Exercise: Add and display a 'cgpa' prop in StudentCard
function StudentCard(props) {
  return (
    <div style={{ border: '1px solid #ccc', padding: '10px', margin: '8px 0' }}>
      <h3>{props.name}</h3>
      <p>Department: {props.dept}</p>
      {/* TODO: Display the student's CGPA using props.cgpa */}
      <p>CGPA: {props.cgpa}</p>
    </div>
  );
}

export default function StudentApp() {
  return (
    <div>
      <StudentCard name="Alex" dept="Computer Science" cgpa="8.8" />
    </div>
  );
}
