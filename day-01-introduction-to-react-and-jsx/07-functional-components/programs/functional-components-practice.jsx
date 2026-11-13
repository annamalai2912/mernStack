/**
 * Practical: Building & Composing Functional Components
 */

import React from 'react';

// Component 1: Named Export - Institution Badge
export function InstitutionBadge() {
  return (
    <span style={{ backgroundColor: '#1e3a8a', color: '#fff', padding: '4px 10px', borderRadius: '4px', fontSize: '12px' }}>
      Mohammed Sathak Institutions
    </span>
  );
}

// Component 2: Named Export - Reusable Action Button
export function PrimaryButton({ label, onClick }) {
  return (
    <button
      onClick={onClick}
      style={{ backgroundColor: '#2563eb', color: '#fff', border: 'none', padding: '8px 16px', borderRadius: '6px', cursor: 'pointer' }}
    >
      {label}
    </button>
  );
}

// Component 3: Named Export - Student Profile Card
export function StudentCard() {
  return (
    <div style={{ border: '1px solid #e2e8f0', borderRadius: '8px', padding: '16px', margin: '12px 0', maxWidth: '350px' }}>
      <InstitutionBadge />
      <h3 style={{ margin: '8px 0 4px 0' }}>Mohamed Imran</h3>
      <p style={{ color: '#64748b', margin: '0 0 12px 0' }}>B.E. Computer Science | 2022-2026</p>
      <PrimaryButton label="View Profile" onClick={() => alert("Viewing Profile!")} />
    </div>
  );
}

// Default Export: Root Container Component Composing Children
export default function FunctionalComponentsPractice() {
  return (
    <div style={{ padding: '24px', fontFamily: 'sans-serif' }}>
      <h2>Functional Components Practice</h2>
      <StudentCard />
      <StudentCard />
    </div>
  );
}

