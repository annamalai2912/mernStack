/**
 * Exercise: Tracing & Customizing the React Root Mount
 * 
 * Task:
 * 1. Inspect what happens if you change <div id="root"> to <div id="app"> in index.html.
 * 2. Update the mounting script below to match the new ID.
 * 3. Add a second component <Footer /> rendered inside the root container.
 */

import React from 'react';
import ReactDOM from 'react-dom/client';

function AppHeader() {
  return <header><h1>Mohammed Sathak Institution</h1></header>;
}

function AppFooter() {
  // TODO: Build a simple footer component with current year and copyright
  return <footer><p>© {new Date().getFullYear()} Mohammed Sathak Institutions. All Rights Reserved.</p></footer>;
}

// TODO: Verify mounting logic
const targetContainer = document.getElementById('root'); // What if this was 'app'?

if (targetContainer) {
  ReactDOM.createRoot(targetContainer).render(
    <React.StrictMode>
      <AppHeader />
      <AppFooter />
    </React.StrictMode>
  );
}

