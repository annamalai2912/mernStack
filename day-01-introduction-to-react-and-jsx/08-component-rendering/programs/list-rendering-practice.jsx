/**
 * Practical: List Rendering & Component Composition
 */

import React from 'react';

// Sample dataset of students
const studentList = [
  { id: "MS-01", name: "Aarav Kumar", dept: "CSE", cgpa: 8.9, skills: ["React", "JS"] },
  { id: "MS-02", name: "Fatima Syed", dept: "IT", cgpa: 9.3, skills: ["React", "Python"] },
  { id: "MS-03", name: "Karthik Raj", dept: "ECE", cgpa: 7.8, skills: ["Embedded", "C++"] },
  { id: "MS-04", name: "Nourin Banu", dept: "AIDS", cgpa: 9.1, skills: ["React", "ML"] }
];

// Child Component: Single Student Row
function StudentRow({ student }) {
  return (
    <tr style={{ borderBottom: '1px solid #e2e8f0' }}>
      <td style={{ padding: '10px' }}>{student.id}</td>
      <td style={{ padding: '10px', fontWeight: 'bold' }}>{student.name}</td>
      <td style={{ padding: '10px' }}>{student.dept}</td>
      <td style={{ padding: '10px' }}>{student.cgpa}</td>
      <td style={{ padding: '10px' }}>
        {student.skills.map((skill) => (
          <span
            key={skill}
            style={{ backgroundColor: '#e0f2fe', color: '#0369a1', padding: '2px 8px', borderRadius: '4px', fontSize: '12px', marginRight: '4px' }}
          >
            {skill}
          </span>
        ))}
      </td>
    </tr>
  );
}

// Parent Component Rendering the Dynamic List
export default function ListRenderingPractice() {
  return (
    <div style={{ padding: '24px', fontFamily: 'sans-serif' }}>
      <h2>Student Directory (Dynamic List Rendering)</h2>
      <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', border: '1px solid #cbd5e1' }}>
        <thead style={{ backgroundColor: '#f8fafc' }}>
          <tr>
            <th style={{ padding: '10px' }}>Roll No</th>
            <th style={{ padding: '10px' }}>Student Name</th>
            <th style={{ padding: '10px' }}>Department</th>
            <th style={{ padding: '10px' }}>CGPA</th>
            <th style={{ padding: '10px' }}>Skills</th>
          </tr>
        </thead>
        <tbody>
          {/* Practical Practice: Mapping over array with unique key */}
          {studentList.map((student) => (
            <StudentRow key={student.id} student={student} />
          ))}
        </tbody>
      </table>
    </div>
  );
}

