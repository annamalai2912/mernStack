import React from 'react';

// Exercise: Add a Footer component and display it inside App
function Footer() {
  // TODO: Return a footer tag with a copyright notice
  return <footer><p>© 2026 Student Portal</p></footer>;
}

export default function App() {
  return (
    <div>
      <h1>Campus Student Portal</h1>
      <p>Welcome to your academic home page.</p>
      {/* Render the Footer component below */}
      <Footer />
    </div>
  );
}
