/**
 * Functional Components Examples
 */

import React from 'react';

// 1. Simple Presentational Component
export function CollegeBadge() {
  return (
    <div style={{ display: 'inline-block', padding: '4px 8px', backgroundColor: '#e0e7ff', color: '#3730a3', borderRadius: '4px', fontSize: '12px' }}>
      Mohammed Sathak Institutions
    </div>
  );
}

// 2. Component Composition (Parent containing Children)
export function StudentAvatar() {
  return (
    <div style={{ width: '60px', height: '60px', borderRadius: '50%', backgroundColor: '#0284c7', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontSize: '24px', fontWeight: 'bold' }}>
      MS
    </div>
  );
}

export default function StudentHeader() {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: '16px', padding: '16px', borderBottom: '1px solid #e2e8f0' }}>
      <StudentAvatar />
      <div>
        <h2 style={{ margin: 0 }}>Student Profile Portal</h2>
        <CollegeBadge />
      </div>
    </div>
  );
}
