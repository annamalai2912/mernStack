/**
 * Practical: Practicing JSX Syntax, Expressions & Rules
 */

import React from 'react';

export default function JsxSyntaxPractice() {
  // 1. JavaScript variables to embed in JSX
  const studentName = "Amina";
  const departmentName = "Computer Science & Engineering";
  const semester = 6;
  const attendance = 88;
  const isEligible = attendance >= 75;

  // 2. Inline style object
  const badgeStyle = {
    padding: '4px 10px',
    borderRadius: '6px',
    display: 'inline-block',
    fontSize: '13px',
    fontWeight: 'bold',
    backgroundColor: isEligible ? '#dcfce7' : '#fee2e2',
    color: isEligible ? '#15803d' : '#b91c1c'
  };

  return (
    // Rule 1: Single root parent element using React Fragment
    <>
      <div style={{ padding: '24px', fontFamily: 'sans-serif', maxWidth: '480px', border: '1px solid #cbd5e1', borderRadius: '10px' }}>
        {/* Rule 2: camelCase className instead of class */}
        <h1 className="main-title" style={{ color: '#1e40af', fontSize: '22px' }}>JSX Syntax Practice</h1>

        {/* Dynamic JS Expressions using curly braces {} */}
        <h2>Student: {studentName.toUpperCase()}</h2>
        <p><strong>Department:</strong> {departmentName}</p>
        <p><strong>Current Semester:</strong> Semester {semester}</p>
        <p><strong>Graduation Year:</strong> {new Date().getFullYear() + 1}</p>

        {/* Conditional Rendering: Ternary Operator */}
        <p style={{ marginTop: '12px' }}>
          <strong>Attendance:</strong> {attendance}% &nbsp;
          <span style={badgeStyle}>
            {isEligible ? "Eligible for Exams" : "Attendance Shortage"}
          </span>
        </p>

        {/* Conditional Rendering: Logical AND (&&) */}
        {isEligible && (
          <p style={{ color: '#0369a1', background: '#e0f2fe', padding: '8px 12px', borderRadius: '6px', fontSize: '13px' }}>
            🎉 Examination hall ticket is unlocked!
          </p>
        )}

        {/* Rule 3: Self-closing input tag */}
        <div style={{ marginTop: '16px' }}>
          <label style={{ display: 'block', fontSize: '13px', marginBottom: '4px' }}>Course Feedback:</label>
          <input
            type="text"
            placeholder="Enter feedback..."
            style={{ width: '100%', padding: '8px', borderRadius: '6px', border: '1px solid #cbd5e1', boxSizing: 'border-box' }}
          />
        </div>
      </div>
    </>
  );
}
