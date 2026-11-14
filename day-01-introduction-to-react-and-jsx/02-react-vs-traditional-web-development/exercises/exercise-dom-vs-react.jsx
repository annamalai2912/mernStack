/**
 * Exercise: Convert Imperative Toggle to Declarative React Component
 * 
 * Task:
 * In traditional JavaScript (imperative), you would write:
 *   const box = document.getElementById('box');
 *   box.style.display = box.style.display === 'none' ? 'block' : 'none';
 * 
 * Your Goal:
 * Complete the React component below to toggle the visibility of the student notice
 * using declarative state (no document.getElementById!).
 */

import React, { useState } from 'react';

export default function ToggleNoticeExercise() {
  const [isVisible, setIsVisible] = useState(true);

  const handleToggle = () => {
    // TODO: Toggle isVisible between true and false
    setIsVisible(!isVisible);
  };

  return (
    <div style={{ padding: '20px', border: '1px solid #cbd5e1', borderRadius: '8px', maxWidth: '380px', fontFamily: 'sans-serif' }}>
      <h3>Campus Student Notice Board</h3>

      <button
        onClick={handleToggle}
        style={{ padding: '8px 16px', background: '#2563eb', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer', marginBottom: '12px' }}
      >
        {isVisible ? "Hide Notice" : "Show Notice"}
      </button>

      {/* Conditionally render this paragraph when isVisible is true */}
      {isVisible && (
        <div style={{ padding: '12px', backgroundColor: '#fef3c7', borderLeft: '4px solid #f59e0b', borderRadius: '4px' }}>
          <p style={{ margin: 0, fontWeight: 'bold', color: '#92400e' }}>📢 Academic Notice</p>
          <p style={{ margin: '4px 0 0 0', color: '#78350f', fontSize: '13px' }}>
            React Practical Lab submissions are due by 5:00 PM today.
          </p>
        </div>
      )}
    </div>
  );
}
