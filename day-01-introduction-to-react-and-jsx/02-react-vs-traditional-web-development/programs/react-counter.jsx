/**
 * Practical: React Declarative UI Component
 * 
 * Notice: No document.getElementById, no manual innerText updates.
 * You declare the UI for the current state, and React handles the DOM.
 */

import React, { useState } from 'react';

export default function ReactCounter() {
  const [count, setCount] = useState(0);

  return (
    <div style={{ border: '1px solid #ccc', padding: '16px', borderRadius: '8px', maxWidth: '300px', fontFamily: 'sans-serif' }}>
      <h2>React Declarative Counter</h2>
      <p>Current Count: {count}</p>
      
      <button onClick={() => setCount(count + 1)} style={{ padding: '8px 16px', marginRight: '8px', cursor: 'pointer' }}>
        + Increment
      </button>

      <button onClick={() => setCount(0)} style={{ padding: '8px 16px', cursor: 'pointer' }}>
        Reset
      </button>
    </div>
  );
}

