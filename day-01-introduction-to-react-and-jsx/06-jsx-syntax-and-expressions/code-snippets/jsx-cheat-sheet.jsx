/**
 * JSX Quick Reference Snippets
 */

import React from 'react';

export default function JsxReference() {
  const collegeName = "Mohammed Sathak";
  const establishedYear = 1973;
  const isAutonomous = true;
  const departments = ["CSE", "IT", "ECE", "MECH", "CIVIL"];

  const cardStyle = {
    padding: '20px',
    borderRadius: '10px',
    backgroundColor: '#f8fafc',
    border: '1px solid #e2e8f0',
    maxWidth: '450px',
    margin: '20px auto',
    fontFamily: 'sans-serif'
  };

  return (
    // 1. Single Root using React Fragment
    <>
      <div style={cardStyle}>
        {/* 2. Embedding Variables & JS Expressions */}
        <h2 style={{ color: '#0f172a', margin: '0 0 8px 0' }}>{collegeName}</h2>
        <p>Age: {new Date().getFullYear() - establishedYear} Years of Excellence</p>

        {/* 3. Conditional Rendering with Ternary & Logical AND */}
        <p>
          Status:{' '}
          <span style={{ fontWeight: 'bold', color: isAutonomous ? '#16a34a' : '#64748b' }}>
            {isAutonomous ? 'Autonomous Institution' : 'Affiliated'}
          </span>
        </p>

        {isAutonomous && (
          <div style={{ backgroundColor: '#dcfce7', color: '#15803d', padding: '6px 12px', borderRadius: '4px' }}>
            Accredited by NAAC with 'A' Grade
          </div>
        )}

        {/* 4. Rendering Lists */}
        <h4>Departments:</h4>
        <ul>
          {departments.map((dept, index) => (
            <li key={index}>{dept}</li>
          ))}
        </ul>

        {/* 5. Self-closing inputs & camelCase handlers */}
        <input
          type="text"
          placeholder="Search student..."
          className="search-input"
          onChange={(e) => console.log(e.target.value)}
        />
      </div>
    </>
  );
}
