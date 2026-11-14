// Child Component: Reusable Student Card
function StudentCard(props) {
  return (
    <div style={{ border: '1px solid #ccc', padding: '10px', margin: '10px 0', borderRadius: '6px' }}>
      <h3>{props.name}</h3>
      <p>Department: {props.dept}</p>
    </div>
  );
}

// Parent Component: Composing Child Components
export default function FunctionalComponentsPractice() {
  return (
    <div style={{ fontFamily: 'sans-serif', padding: '20px' }}>
      <h2>Student Directory</h2>
      <StudentCard name="Amina" dept="Computer Science" />
      <StudentCard name="Rahul" dept="Information Technology" />
    </div>
  );
}
