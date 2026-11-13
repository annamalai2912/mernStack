/**
 * Practical: Understanding how React binds to index.html
 * 
 * Trace how main.jsx finds the <div id="root"> element and renders the root component.
 */

import React from 'react';
import ReactDOM from 'react-dom/client';

// Simple custom component to test root rendering
function MyRootApp() {
  return (
    <div style={{ fontFamily: 'sans-serif', padding: '20px' }}>
      <h1>Mohammed Sathak React App</h1>
      <p>Project Structure Verified: main.jsx mounted into index.html</p>
    </div>
  );
}

// Practical mounting code:
const rootElement = document.getElementById('root');

if (rootElement) {
  ReactDOM.createRoot(rootElement).render(
    <React.StrictMode>
      <MyRootApp />
    </React.StrictMode>
  );
}

