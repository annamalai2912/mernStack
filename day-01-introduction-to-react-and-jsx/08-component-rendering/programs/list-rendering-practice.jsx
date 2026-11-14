// Practical: List Rendering with .map() and key
export default function ListRenderingPractice() {
  const students = [
    { id: 1, name: "Aarav", dept: "CSE" },
    { id: 2, name: "Fatima", dept: "IT" },
    { id: 3, name: "Karthik", dept: "ECE" }
  ];

  return (
    <div style={{ fontFamily: 'sans-serif', padding: '20px' }}>
      <h2>Student Directory</h2>
      <ul>
        {students.map((student) => (
          <li key={student.id}>
            <strong>{student.name}</strong> - {student.dept}
          </li>
        ))}
      </ul>
    </div>
  );
}
