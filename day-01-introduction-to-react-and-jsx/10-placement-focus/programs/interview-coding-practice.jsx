/**
 * Placement Technical Interview: Coding Challenges
 * 
 * Commonly asked live-coding questions in fresher technical interviews.
 */

import React, { useState } from 'react';

// =========================================================================
// CHALLENGE 1: Render List with Unique Keys & Conditional Badges
// Question: "Given an array of placement candidates, render them with a status
// badge showing 'Selected' in green or 'In Process' in orange."
// =========================================================================
const initialCandidates = [
  { id: "C01", name: "Aarav", role: "Frontend Dev", status: "Selected" },
  { id: "C02", name: "Fatima", role: "Full Stack Dev", status: "In Process" },
  { id: "C03", name: "Karthik", role: "React Engineer", status: "Selected" },
  { id: "C04", name: "Zainab", role: "UI/UX Developer", status: "In Process" }
];

export function CandidateListChallenge() {
  return (
    <div style={{ padding: '16px', background: '#fff', border: '1px solid #e2e8f0', borderRadius: '8px', marginBottom: '16px' }}>
      <h3 style={{ margin: '0 0 8px 0', color: '#1e293b' }}>1. Placement Candidate Tracker</h3>
      <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
        {initialCandidates.map((candidate) => (
          <li key={candidate.id} style={{ padding: '8px 0', borderBottom: '1px solid #f1f5f9', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span>
              <strong>{candidate.name}</strong> - <span style={{ color: '#64748b', fontSize: '13px' }}>{candidate.role}</span>
            </span>
            <span style={{
              padding: '3px 8px',
              borderRadius: '4px',
              fontSize: '12px',
              fontWeight: 'bold',
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
// CHALLENGE 2: Functional Counter with Bounds (Min: 0, Max: 10)
// Question: "Build a counter component in React that increments and decrements,
// but prevents going below 0 or above 10, disabling buttons appropriately."
// =========================================================================
export function BoundedCounterChallenge() {
  const [count, setCount] = useState(0);

  return (
    <div style={{ padding: '16px', background: '#fff', border: '1px solid #e2e8f0', borderRadius: '8px', marginBottom: '16px' }}>
      <h3 style={{ margin: '0 0 8px 0', color: '#1e293b' }}>2. Bounded Counter (Range 0 - 10)</h3>
      <p style={{ fontSize: '18px', fontWeight: 'bold', margin: '8px 0' }}>Score: {count}</p>
      
      <button
        onClick={() => setCount(count - 1)}
        disabled={count <= 0}
        style={{ padding: '6px 14px', marginRight: '8px', cursor: count <= 0 ? 'not-allowed' : 'pointer', background: count <= 0 ? '#cbd5e1' : '#e2e8f0' }}
      >
        - Decrement
      </button>

      <button
        onClick={() => setCount(count + 1)}
        disabled={count >= 10}
        style={{ padding: '6px 14px', marginRight: '8px', cursor: count >= 10 ? 'not-allowed' : 'pointer', background: count >= 10 ? '#93c5fd' : '#2563eb', color: '#fff' }}
      >
        + Increment
      </button>

      <button
        onClick={() => setCount(0)}
        style={{ padding: '6px 14px', background: '#fee2e2', color: '#b91c1c', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
      >
        Reset
      </button>

      {count === 10 && <p style={{ color: '#dc2626', fontSize: '13px', margin: '8px 0 0 0' }}>⚠️ Maximum limit of 10 reached!</p>}
      {count === 0 && <p style={{ color: '#64748b', fontSize: '13px', margin: '8px 0 0 0' }}>ℹ️ Minimum limit of 0 reached.</p>}
    </div>
  );
}

// =========================================================================
// CHALLENGE 3: Real-Time Search Filter
// Question: "Given a list of technical skills, provide a real-time text input
// that filters the displayed skills based on user typing."
// =========================================================================
export function RealTimeSearchChallenge() {
  const allSkills = ["React", "JavaScript", "Node.js", "Express", "MongoDB", "Tailwind CSS", "Git", "REST APIs"];
  const [searchTerm, setSearchTerm] = useState("");

  const filteredSkills = allSkills.filter(skill =>
    skill.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div style={{ padding: '16px', background: '#fff', border: '1px solid #e2e8f0', borderRadius: '8px' }}>
      <h3 style={{ margin: '0 0 8px 0', color: '#1e293b' }}>3. Real-Time Skill Filter</h3>
      <input
        type="text"
        placeholder="Filter skills (e.g. 'react', 'git')..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        style={{ width: '100%', padding: '8px 12px', border: '1px solid #cbd5e1', borderRadius: '6px', boxSizing: 'border-box', marginBottom: '12px' }}
      />
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px' }}>
        {filteredSkills.length > 0 ? (
          filteredSkills.map(skill => (
            <span key={skill} style={{ background: '#e0f2fe', color: '#0369a1', padding: '4px 10px', borderRadius: '12px', fontSize: '12px', fontWeight: '500' }}>
              {skill}
            </span>
          ))
        ) : (
          <span style={{ color: '#94a3b8', fontSize: '13px' }}>No matching skills found.</span>
        )}
      </div>
    </div>
  );
}

// Master Composed Component
export default function InterviewCodingPractice() {
  return (
    <div style={{ maxWidth: '520px', margin: '20px auto', fontFamily: 'sans-serif' }}>
      <h2 style={{ color: '#0f172a' }}>Placement Technical Interview Challenges</h2>
      <CandidateListChallenge />
      <BoundedCounterChallenge />
      <RealTimeSearchChallenge />
    </div>
  );
}
