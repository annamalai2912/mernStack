/**
 * Complete Component: Student Profile Dashboard
 * 
 * Demonstrates:
 * 1. Composing multiple functional components (ProfileHeader, AcademicStats, SkillsCard, ContactCard)
 * 2. Dynamic JSX expressions and inline styling
 * 3. Conditional rendering (Ternary operator, logical AND)
 * 4. List rendering using .map() with unique keys
 */

import React from 'react';
import { studentData } from '../student-data.js';

// Section 1: Profile Header Component
export function ProfileHeader({ profile }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: '20px', paddingBottom: '20px', borderBottom: '1px solid #e2e8f0' }}>
      <img
        src={profile.avatar}
        alt={profile.name}
        style={{ width: '84px', height: '84px', borderRadius: '50%', objectFit: 'cover', border: '3px solid #2563eb' }}
      />
      <div>
        <h2 style={{ margin: '0 0 4px 0', color: '#0f172a' }}>{profile.name}</h2>
        <p style={{ margin: '0 0 4px 0', color: '#64748b', fontSize: '14px' }}>
          Roll No: <strong>{profile.rollNo}</strong> | {profile.department}
        </p>
        <p style={{ margin: '0 0 6px 0', color: '#1e40af', fontSize: '13px', fontWeight: '500' }}>
          {profile.institution} ({profile.batch})
        </p>
        <p style={{ margin: 0, color: '#475569', fontSize: '13px', fontStyle: 'italic' }}>"{profile.bio}"</p>
      </div>
    </div>
  );
}

// Section 2: Academic Statistics Component
export function AcademicStats({ academics }) {
  const isExamEligible = academics.attendance >= 75;

  return (
    <div style={{ marginTop: '20px' }}>
      <h3 style={{ margin: '0 0 12px 0', color: '#1e293b' }}>Academic Standing ({academics.semester})</h3>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(130px, 1fr))', gap: '12px' }}>
        
        {/* CGPA Card */}
        <div style={{ background: '#f8fafc', padding: '12px', borderRadius: '8px', border: '1px solid #e2e8f0', textAlign: 'center' }}>
          <p style={{ margin: '0 0 4px 0', fontSize: '12px', color: '#64748b' }}>Cumulative GPA</p>
          <p style={{ margin: 0, fontSize: '20px', fontWeight: 'bold', color: '#16a34a' }}>{academics.cgpa} / 10</p>
        </div>

        {/* Attendance Card */}
        <div style={{ background: '#f8fafc', padding: '12px', borderRadius: '8px', border: '1px solid #e2e8f0', textAlign: 'center' }}>
          <p style={{ margin: '0 0 4px 0', fontSize: '12px', color: '#64748b' }}>Attendance</p>
          <p style={{ margin: 0, fontSize: '20px', fontWeight: 'bold', color: isExamEligible ? '#2563eb' : '#dc2626' }}>
            {academics.attendance}%
          </p>
        </div>

        {/* Exam Eligibility Card */}
        <div style={{ background: '#f8fafc', padding: '12px', borderRadius: '8px', border: '1px solid #e2e8f0', textAlign: 'center' }}>
          <p style={{ margin: '0 0 4px 0', fontSize: '12px', color: '#64748b' }}>Exam Status</p>
          <span style={{
            display: 'inline-block',
            marginTop: '2px',
            padding: '3px 8px',
            borderRadius: '4px',
            fontSize: '11px',
            fontWeight: 'bold',
            background: isExamEligible ? '#dcfce7' : '#fee2e2',
            color: isExamEligible ? '#15803d' : '#991b1b'
          }}>
            {isExamEligible ? "ELIGIBLE" : "SHORTAGE"}
          </span>
        </div>

        {/* Placement Status Card */}
        <div style={{ background: '#f8fafc', padding: '12px', borderRadius: '8px', border: '1px solid #e2e8f0', textAlign: 'center' }}>
          <p style={{ margin: '0 0 4px 0', fontSize: '12px', color: '#64748b' }}>Placements</p>
          <p style={{ margin: 0, fontSize: '14px', fontWeight: 'bold', color: '#d97706' }}>
            {academics.isPlacementEligible ? "Registered" : "Not Eligible"}
          </p>
        </div>

      </div>
    </div>
  );
}

// Section 3: Technical Skills Component
export function SkillsSection({ skills }) {
  return (
    <div style={{ marginTop: '20px' }}>
      <h3 style={{ margin: '0 0 10px 0', color: '#1e293b' }}>Technical Skills ({skills.length})</h3>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
        {skills.map((skill) => (
          <span
            key={skill}
            style={{
              background: '#e0f2fe',
              color: '#0369a1',
              padding: '6px 12px',
              borderRadius: '20px',
              fontSize: '13px',
              fontWeight: '500'
            }}
          >
            {skill}
          </span>
        ))}
      </div>
    </div>
  );
}

// Section 4: Contact Action Component
export function ContactFooter({ contact }) {
  return (
    <div style={{ marginTop: '24px', paddingTop: '16px', borderTop: '1px solid #e2e8f0', display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
      <a
        href={`mailto:${contact.email}`}
        style={{ textDecoration: 'none', background: '#2563eb', color: '#fff', padding: '8px 14px', borderRadius: '6px', fontSize: '13px', fontWeight: '500' }}
      >
        📧 Email Student
      </a>
      <a
        href={contact.github}
        target="_blank"
        rel="noreferrer"
        style={{ textDecoration: 'none', background: '#0f172a', color: '#fff', padding: '8px 14px', borderRadius: '6px', fontSize: '13px', fontWeight: '500' }}
      >
        🐙 GitHub Profile
      </a>
      <a
        href={contact.linkedin}
        target="_blank"
        rel="noreferrer"
        style={{ textDecoration: 'none', background: '#0284c7', color: '#fff', padding: '8px 14px', borderRadius: '6px', fontSize: '13px', fontWeight: '500' }}
      >
        💼 LinkedIn
      </a>
    </div>
  );
}

// Main Composed Dashboard Component
export default function StudentProfileDashboard() {
  return (
    <div style={{ maxWidth: '680px', margin: '20px auto', background: '#ffffff', border: '1px solid #cbd5e1', borderRadius: '12px', padding: '24px', boxShadow: '0 4px 6px -1px rgba(0,0,0,0.08)', fontFamily: 'sans-serif' }}>
      <ProfileHeader profile={studentData.profile} />
      <AcademicStats academics={studentData.academics} />
      <SkillsSection skills={studentData.skills} />
      <ContactFooter contact={studentData.contact} />
    </div>
  );
}
