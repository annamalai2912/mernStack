import { studentData } from './student-data.js';

// Practical: Simple Student Profile Dashboard Component
export default function StudentProfileDashboard() {
  return (
    <div style={{ fontFamily: 'sans-serif', padding: '20px', maxWidth: '350px', border: '1px solid #ccc', borderRadius: '8px' }}>
      <h2>{studentData.name}</h2>
      <p><strong>Roll No:</strong> {studentData.rollNo}</p>
      <p><strong>Department:</strong> {studentData.dept}</p>
      <p><strong>CGPA:</strong> {studentData.cgpa}</p>
      <p><strong>Attendance:</strong> {studentData.attendance}%</p>

      <h3>Skills:</h3>
      <ul>
        {studentData.skills.map((skill) => (
          <li key={skill}>{skill}</li>
        ))}
      </ul>
    </div>
  );
}
