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
    <div style={{ border: '1px solid #cbd5e1', padding: '20px', borderRadius: '8px', maxWidth: '320px', fontFamily: 'sans-serif', background: '#fff' }}>
      <h2>React Declarative Counter</h2>
      <p style={{ color: '#64748b', fontSize: '13px' }}>State-driven: UI re-renders automatically</p>
      <p style={{ fontSize: '24px', fontWeight: 'bold', margin: '12px 0' }}>Current Count: {count}</p>
      
      <button
        onClick={() => setCount(count + 1)}
        style={{ padding: '8px 14px', marginRight: '6px', background: '#2563eb', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
      >
        + Increment
      </button>

      <button
        onClick={() => setCount(count - 1)}
        style={{ padding: '8px 14px', marginRight: '6px', background: '#e2e8f0', color: '#1e293b', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
      >
        - Decrement
      </button>

      <button
        onClick={() => setCount(0)}
        style={{ padding: '8px 14px', background: '#fee2e2', color: '#b91c1c', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
      >
        Reset
      </button>
    </div>
  );
}
