import React from 'react';
import ReactDOM from 'react-dom/client';

// Simple Root Component
function App() {
  return (
    <div style={{ fontFamily: 'sans-serif', padding: '20px' }}>
      <h1>Student Portal</h1>
      <p>React is successfully mounted into index.html!</p>
    </div>
  );
}

// Mount to <div id="root">
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);

export default App;
