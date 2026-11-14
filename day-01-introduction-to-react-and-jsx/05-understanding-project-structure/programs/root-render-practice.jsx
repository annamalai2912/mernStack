/**
 * Practical: Understanding How React Binds to index.html
 * 
 * Trace how main.jsx finds the <div id="root"> element and renders the root component.
 */

import React from 'react';
import ReactDOM from 'react-dom/client';

// Simple custom component to test root rendering
function CampusRootApp() {
  return (
    <div style={{ fontFamily: 'sans-serif', padding: '24px', maxWidth: '500px', border: '1px solid #cbd5e1', borderRadius: '8px' }}>
      <h1 style={{ color: '#1e40af' }}>Campus Student Portal</h1>
      <p style={{ color: '#475569' }}>
        <strong>Project Structure Verified:</strong> <code>main.jsx</code> successfully mounted <code>&lt;App /&gt;</code> into <code>index.html</code>'s <code>&lt;div id="root"&gt;</code>.
      </p>
      <div style={{ marginTop: '16px', padding: '12px', background: '#f1f5f9', borderRadius: '6px' }}>
        <p style={{ margin: 0, fontSize: '13px', color: '#334155' }}>
          <strong>Mounting Method:</strong> <code>ReactDOM.createRoot(container).render(&lt;Component /&gt;)</code>
        </p>
      </div>
    </div>
  );
}

// Practical mounting code:
const rootElement = document.getElementById('root');

if (rootElement) {
  ReactDOM.createRoot(rootElement).render(
    <React.StrictMode>
      <CampusRootApp />
    </React.StrictMode>
  );
}

export default CampusRootApp;
