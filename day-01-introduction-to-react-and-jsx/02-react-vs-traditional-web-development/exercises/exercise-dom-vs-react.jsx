/**
 * Exercise: Convert Imperative Toggle to Declarative React Component
 * 
 * Task:
 * In traditional JavaScript, you would do:
 *   const box = document.getElementById('box');
 *   box.style.display = box.style.display === 'none' ? 'block' : 'none';
 * 
 * Your Goal:
 * Complete the React component below to toggle the visibility of the message
 * using declarative state (no document.getElementById!).
 */

import React, { useState } from 'react';

export default function ToggleMessageExercise() {
  const [isVisible, setIsVisible] = useState(true);

  const handleToggle = () => {
    // TODO: Toggle isVisible between true and false
  };

  return (
    <div style={{ padding: '20px', border: '1px solid #ccc', borderRadius: '8px', maxWidth: '350px' }}>
      <h3>Student Notice Board</h3>

      <button onClick={handleToggle} style={{ padding: '8px 16px', cursor: 'pointer' }}>
        {isVisible ? "Hide Notice" : "Show Notice"}
      </button>

      {/* TODO: Conditionally render this paragraph when isVisible is true */}
      {isVisible && (
        <p style={{ marginTop: '12px', padding: '10px', backgroundColor: '#fef3c7', borderRadius: '4px' }}>
          📢 Day 1 React Practical submissions are due by 5:00 PM!
        </p>
      )}
    </div>
  );
}
