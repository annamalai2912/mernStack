/**
 * Practical: Building & Composing Functional Components
 */

import React from 'react';

// Component 1: Named Export - Department / Campus Badge
export function DepartmentBadge() {
  return (
    <span style={{ backgroundColor: '#1e3a8a', color: '#fff', padding: '4px 10px', borderRadius: '4px', fontSize: '12px', fontWeight: 'bold' }}>
      Computer Science & Engineering
    </span>
  );
}

// Component 2: Named Export - Reusable Action Button
export function PrimaryButton({ label, onClick }) {
  return (
    <button
      onClick={onClick}
      style={{ backgroundColor: '#2563eb', color: '#fff', border: 'none', padding: '8px 16px', borderRadius: '6px', cursor: 'pointer', fontSize: '13px' }}
    >
      {label}
    </button>
  );
}

// Component 3: Named Export - Student Profile Card Composing Badge and Button
export function StudentCard({ name = "Rohan Sharma", batch = "2022-2026", rollNo = "CS-2024-088" }) {
  return (
    <div style={{ border: '1px solid #e2e8f0', borderRadius: '8px', padding: '16px', margin: '12px 0', maxWidth: '360px', background: '#fff', boxShadow: '0 2px 4px rgba(0,0,0,0.04)' }}>
      <DepartmentBadge />
      <h3 style={{ margin: '10px 0 4px 0', color: '#0f172a' }}>{name}</h3>
      <p style={{ color: '#64748b', fontSize: '13px', margin: '0 0 12px 0' }}>Roll No: {rollNo} | Batch: {batch}</p>
      <PrimaryButton label="View Academic Details" onClick={() => alert(`Viewing details for ${name}`)} />
    </div>
  );
}

// Default Export: Root Container Component Composing Children
export default function FunctionalComponentsPractice() {
  return (
    <div style={{ padding: '24px', fontFamily: 'sans-serif', background: '#f8fafc' }}>
      <h2>Functional Components & Composition</h2>
      <p style={{ color: '#64748b' }}>Breaking UI into reusable, composable building blocks:</p>
      <StudentCard name="Rohan Sharma" rollNo="CS-2024-088" />
      <StudentCard name="Priya Sundaram" rollNo="CS-2024-092" />
    </div>
  );
}
