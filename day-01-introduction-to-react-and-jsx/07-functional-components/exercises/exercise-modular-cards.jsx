/**
 * Exercise: Building Modular & Composed Functional Components
 * 
 * Instructions:
 * 1. Build a `DepartmentBadge` functional component that takes `deptName` as a prop.
 * 2. Build a `StatusBadge` functional component that displays "Active Student".
 * 3. Compose both inside `StudentDirectoryCard`.
 * 4. Ensure all components follow PascalCase and export rules.
 */

import React from 'react';

// TODO: Create DepartmentBadge component
export function DepartmentBadge({ deptName }) {
  return (
    <span style={{ backgroundColor: '#e2e8f0', color: '#1e293b', padding: '4px 8px', borderRadius: '4px', fontSize: '12px' }}>
      {deptName}
    </span>
  );
}

// TODO: Create StatusBadge component
export function StatusBadge({ status = "Active Student" }) {
  return (
    <span style={{ backgroundColor: '#dcfce7', color: '#15803d', padding: '4px 8px', borderRadius: '4px', fontSize: '12px', marginLeft: '6px' }}>
      {status}
    </span>
  );
}

// TODO: Compose into main StudentDirectoryCard
export default function StudentDirectoryCard() {
  return (
    <div style={{ border: '1px solid #cbd5e1', borderRadius: '8px', padding: '16px', maxWidth: '320px', fontFamily: 'sans-serif' }}>
      <h3>Rashid Khan</h3>
      <div style={{ marginBottom: '12px' }}>
        <DepartmentBadge deptName="Computer Science & Engineering" />
        <StatusBadge status="Active Student" />
      </div>
      <p style={{ color: '#64748b', fontSize: '14px' }}>Year: 3rd Year | Roll: 911521104033</p>
    </div>
  );
}

