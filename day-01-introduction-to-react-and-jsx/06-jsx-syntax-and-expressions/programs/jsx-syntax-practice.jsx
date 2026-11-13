/**
 * Practical: Practicing JSX Syntax, Expressions & Rules
 */

import React from 'react';

export default function JsxSyntaxPractice() {
  // 1. JavaScript variables to embed in JSX
  const studentName = "Amina";
  const collegeName = "Mohammed Sathak";
  const semester = 6;
  const attendance = 88;
  const isEligible = attendance >= 75;

  // 2. Inline style object
  const badgeStyle = {
    padding: '6px 12px',
    borderRadius: '6px',
    display: 'inline-block',
    fontSize: '14px',
    fontWeight: 'bold',
    backgroundColor: isEligible ? '#dcfce7' : '#fee2e2',
    color: isEligible ? '#15803d' : '#b91c1c'
  };

  return (
    // Rule: Single root element using React Fragment
    <>
      <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
        {/* Rule: camelCase className */}
        <h1 className="main-title">JSX Syntax Practice</h1>

        {/* Dynamic JS Expressions using {} */}
        <h2>Student: {studentName.toUpperCase()}</h2>
        <p>College: {collegeName}</p>
        <p>Current Semester: {semester}</p>
        <p>Graduation Year: {new Date().getFullYear() + 1}</p>

        {/* Conditional Rendering: Ternary Operator */}
        <p>
          Attendance: {attendance}% -{' '}
          <span style={badgeStyle}>
            {isEligible ? "Eligible for Exams" : "Attendance Shortage"}
          </span>
        </p>

        {/* Conditional Rendering: Logical AND */}
        {isEligible && (
          <p style={{ color: '#0369a1' }}>
            🎉 Hall ticket generation is unlocked!
          </p>
        )}

        {/* Rule: Self-closing input tag */}
        <input
          type="text"
          placeholder="Enter feedback..."
          style={{ padding: '8px', borderRadius: '4px', border: '1px solid #ccc' }}
        />
      </div>
    </>
  );
}

