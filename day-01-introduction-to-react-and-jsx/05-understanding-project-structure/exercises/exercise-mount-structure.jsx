/**
 * Exercise: Tracing & Customizing the React Root Mount
 * 
 * Task:
 * 1. Understand how main.jsx finds the target element in index.html.
 * 2. Add an AppHeader and AppFooter component to build a clean structured layout.
 * 3. Inspect what happens if target element ID does not match index.html.
 */

import React from 'react';
import ReactDOM from 'react-dom/client';

export function AppHeader() {
  return (
    <header style={{ borderBottom: '2px solid #2563eb', paddingBottom: '10px', marginBottom: '16px' }}>
      <h1 style={{ margin: 0, color: '#1e40af', fontSize: '22px' }}>Campus Student Portal</h1>
      <p style={{ margin: '4px 0 0 0', color: '#64748b', fontSize: '13px' }}>Department of Computer Science & Engineering</p>
    </header>
  );
}

export function AppFooter() {
  // Simple footer component with dynamic current year
  return (
    <footer style={{ marginTop: '24px', borderTop: '1px solid #e2e8f0', paddingTop: '12px' }}>
      <p style={{ margin: 0, fontSize: '12px', color: '#94a3b8' }}>
        © {new Date().getFullYear()} University Campus Academic Portal. All Rights Reserved.
      </p>
    </footer>
  );
}

export default function AppLayout() {
  return (
    <div style={{ fontFamily: 'sans-serif', maxWidth: '500px', padding: '20px', border: '1px solid #cbd5e1', borderRadius: '8px' }}>
      <AppHeader />
      <main>
        <h3>Welcome to Student Dashboard</h3>
        <p style={{ color: '#475569' }}>Your courses, grades, and attendance are synced.</p>
      </main>
      <AppFooter />
    </div>
  );
}

// Mounting target verification
const targetContainer = document.getElementById('root');

if (targetContainer) {
  ReactDOM.createRoot(targetContainer).render(
    <React.StrictMode>
      <AppLayout />
    </React.StrictMode>
  );
}
