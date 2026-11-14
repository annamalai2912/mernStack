/**
 * Exercise: Dynamic List Rendering with Keys & Conditional Status
 * 
 * Instructions:
 * 1. Render the `courses` array using JavaScript `.map()`.
 * 2. Ensure each `<tr>` element has a unique `key` prop using `course.code`.
 * 3. Conditionally render the grade badge:
 *    - "PASS" (green background) if score >= 50
 *    - "ARREAR" (red background) if score < 50
 */

import React from 'react';

const courses = [
  { code: "CS8391", name: "Data Structures", credits: 4, score: 78 },
  { code: "CS8392", name: "Database Systems", credits: 3, score: 85 },
  { code: "MA8351", name: "Discrete Mathematics", credits: 4, score: 45 },
  { code: "CS8351", name: "Digital Principles", credits: 3, score: 90 }
];

export default function CourseListExercise() {
  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h2>Semester Course Grade Report</h2>
      <table style={{ width: '100%', borderCollapse: 'collapse', border: '1px solid #cbd5e1' }}>
        <thead>
          <tr style={{ backgroundColor: '#f1f5f9', textAlign: 'left' }}>
            <th style={{ padding: '8px' }}>Code</th>
            <th style={{ padding: '8px' }}>Subject</th>
            <th style={{ padding: '8px' }}>Credits</th>
            <th style={{ padding: '8px' }}>Score</th>
            <th style={{ padding: '8px' }}>Result</th>
          </tr>
        </thead>
        <tbody>
          {/* TODO: Map courses with key={course.code} */}
          {courses.map((course) => (
            <tr key={course.code} style={{ borderBottom: '1px solid #e2e8f0' }}>
              <td style={{ padding: '8px' }}>{course.code}</td>
              <td style={{ padding: '8px' }}>{course.name}</td>
              <td style={{ padding: '8px' }}>{course.credits}</td>
              <td style={{ padding: '8px' }}>{course.score}</td>
              <td style={{ padding: '8px' }}>
                <span style={{
                  padding: '2px 8px',
                  borderRadius: '4px',
                  fontSize: '12px',
                  backgroundColor: course.score >= 50 ? '#dcfce7' : '#fee2e2',
                  color: course.score >= 50 ? '#15803d' : '#b91c1c'
                }}>
                  {course.score >= 50 ? "PASS" : "ARREAR"}
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

