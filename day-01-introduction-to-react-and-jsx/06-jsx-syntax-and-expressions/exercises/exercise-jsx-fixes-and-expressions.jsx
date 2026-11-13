/**
 * Exercise: Fix the Broken JSX & Add Dynamic Expressions
 * 
 * Instructions:
 * The component below has 5 deliberate JSX syntax errors.
 * 1. Find and fix all 5 syntax errors.
 * 2. Calculate the student's final percentage dynamically inside {}.
 * 3. Add conditional rendering: If marks >= 50, show "PASSED", otherwise "NEEDS RETEST".
 */

import React from 'react';

// FIX THIS COMPONENT:
export default function BrokenStudentCard() {
  const student = {
    name: "Farhan Akhtar",
    marksObtained: 420,
    totalMarks: 500
  };

  const percentage = (student.marksObtained / student.totalMarks) * 100;

  return (
    // FIX 1: Missing parent fragment or wrapper element
    // FIX 2: class instead of className
    // FIX 3: unclosed img tag
    // FIX 4: unclosed input tag
    // FIX 5: invalid inline style format
    <div class="card" style="border: 1px solid black; padding: 10px;">
      <h2>Student: {student.name}</h2>
      <img src="https://via.placeholder.com/100" alt="avatar">
      <p>Score: {student.marksObtained} / {student.totalMarks}</p>
      <p>Percentage: {percentage}%</p>
      <p>Result: {percentage >= 50 ? "PASSED" : "NEEDS RETEST"}</p>
      <input type="text" placeholder="Instructor Remarks">
    </div>
  );
}
