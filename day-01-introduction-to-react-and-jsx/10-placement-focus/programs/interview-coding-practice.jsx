/**
 * Placement Technical Interview: Coding Challenges
 * 
 * Commonly asked live-coding questions in fresher technical interviews.
 */

import React, { useState } from 'react';

// =========================================================================
// CHALLENGE 1: Render List with Proper Keys & Conditional Styling
// Question: "Given an array of placement candidates, render them with a badge
// showing 'Selected' in green or 'In Process' in orange."
// =========================================================================
const candidates = [
  { id: "C01", name: "Aarav", status: "Selected" },
  { id: "C02", name: "Fatima", status: "In Process" },
  { id: "C03", name: "Karthik", status: "Selected" },
  { id: "C04", name: "Zainab", status: "In Process" }
];

export function CandidateListChallenge() {
  return (
    <div>
      <h3>Placement Candidate Tracker</h3>
      <ul>
        {candidates.map((candidate) => (
          <li key={candidate.id} style={{ marginBottom: '8px' }}>
            <span>{candidate.name}</span> -{' '}
            <span style={{
              padding: '2px 8px',
              borderRadius: '4px',
              fontSize: '12px',
              backgroundColor: candidate.status === 'Selected' ? '#dcfce7' : '#fef3c7',
              color: candidate.status === 'Selected' ? '#15803d' : '#b45309'
            }}>
              {candidate.status}
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
}

// =========================================================================
// CHALLENGE 2: Functional Counter with Boundaries (Min: 0, Max: 10)
// Question: "Build a counter component in React that increments and decrements,
// but prevents going below 0 or above 10."
// =========================================================================
export function BoundedCounterChallenge() {
  const [count, setCount] = useState(0);

  return (
    <div style={{ marginTop: '20px' }}>
      <h3>Bounded Counter</h3>
      <p>Count: {count}</p>
      <button
        onClick={() => setCount(count - 1)}
        disabled={count <= 0}
        style={{ marginRight: '8px' }}
      >
        - Decrement
      </button>
      <button
        onClick={() => setCount(count + 1)}
        disabled={count >= 10}
      >
        + Increment
      </button>
      {count === 10 && <p style={{ color: 'red' }}>Maximum limit reached!</p>}
      {count === 0 && <p style={{ color: 'gray' }}>Minimum limit reached!</p>}
    </div>
  );
}
