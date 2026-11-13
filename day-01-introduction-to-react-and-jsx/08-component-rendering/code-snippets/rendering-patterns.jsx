/**
 * Component Rendering Patterns
 */

import React from 'react';

const mockStudent = {
  name: "Mohammed Ibrahim",
  rollNo: "911521104001",
  department: "Computer Science and Engineering",
  year: "Final Year (2025)",
  skills: ["React.js", "JavaScript (ES6+)", "Node.js", "Tailwind CSS", "Git"],
  scores: [
    { semester: "Sem 1", gpa: 8.5 },
    { semester: "Sem 2", gpa: 8.7 },
    { semester: "Sem 3", gpa: 8.9 },
    { semester: "Sem 4", gpa: 9.1 }
  ]
};

// Child Component 1: Skill Badge
function SkillBadge({ skill }) {
  return (
    <span style={{
      display: 'inline-block',
      backgroundColor: '#e0f2fe',
      color: '#0369a1',
      padding: '4px 10px',
      borderRadius: '16px',
      fontSize: '12px',
      marginRight: '6px',
      marginBottom: '6px'
    }}>
      {skill}
    </span>
  );
}

// Child Component 2: Semester Score Table
function ScoreTable({ scores }) {
  return (
    <table style={{ width: '100%', borderCollapse: 'collapse', marginTop: '10px' }}>
      <thead>
        <tr style={{ backgroundColor: '#f1f5f9', textAlign: 'left' }}>
          <th style={{ padding: '8px', border: '1px solid #cbd5e1' }}>Semester</th>
          <th style={{ padding: '8px', border: '1px solid #cbd5e1' }}>GPA</th>
        </tr>
      </thead>
      <tbody>
        {scores.map((s, index) => (
          <tr key={s.semester}>
            <td style={{ padding: '8px', border: '1px solid #cbd5e1' }}>{s.semester}</td>
            <td style={{ padding: '8px', border: '1px solid #cbd5e1' }}>{s.gpa}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

// Parent Component
export default function StudentProfileView() {
  return (
    <div style={{ maxWidth: '500px', margin: '20px auto', padding: '24px', border: '1px solid #e2e8f0', borderRadius: '12px', fontFamily: 'system-ui, sans-serif' }}>
      <h2 style={{ margin: '0 0 4px 0' }}>{mockStudent.name}</h2>
      <p style={{ color: '#64748b', margin: '0 0 16px 0' }}>{mockStudent.rollNo} | {mockStudent.department}</p>
      
      <h4>Technical Skills:</h4>
      <div>
        {mockStudent.skills.map((skill) => (
          <SkillBadge key={skill} skill={skill} />
        ))}
      </div>

      <h4>Academic History:</h4>
      <ScoreTable scores={mockStudent.scores} />
    </div>
  );
}
