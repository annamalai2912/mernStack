/**
 * Starter mock data for the Student Profile Dashboard
 * You can customize this with your real information!
 */

export const studentProfile = {
  personalInfo: {
    fullName: "Ayesha Banu",
    avatarUrl: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=300&q=80",
    rollNo: "911521104042",
    regNo: "MS-CSE-2022-042",
    institution: "Mohammed Sathak Engineering College",
    department: "Computer Science & Engineering",
    batch: "2022 - 2026",
    semester: "Semester 6",
    bio: "Passionate aspiring full-stack developer with keen interest in React, modern JavaScript, and building accessible web applications."
  },
  academics: {
    cgpa: 8.92,
    attendancePercentage: 94,
    placementEligible: true,
    standingBacklogs: 0,
    semesterScores: [
      { sem: "Sem 1", gpa: 8.6 },
      { sem: "Sem 2", gpa: 8.8 },
      { sem: "Sem 3", gpa: 9.1 },
      { sem: "Sem 4", gpa: 8.9 },
      { sem: "Sem 5", gpa: 9.2 }
    ]
  },
  skills: [
    { name: "React.js", category: "Frontend", level: "Beginner" },
    { name: "JavaScript (ES6+)", category: "Language", level: "Intermediate" },
    { name: "HTML5 & CSS3", category: "Frontend", level: "Advanced" },
    { name: "Node.js Basics", category: "Backend", level: "Beginner" },
    { name: "Git & GitHub", category: "DevOps", level: "Intermediate" },
    { name: "SQL & Databases", category: "Database", level: "Intermediate" }
  ],
  projects: [
    {
      id: 1,
      title: "Campus Event Management System",
      tech: "HTML, CSS, JS",
      description: "A responsive portal to register and track college cultural and technical events."
    },
    {
      id: 2,
      title: "Student Profile Dashboard",
      tech: "React, Vite, JSX",
      description: "Interactive dashboard displaying student credentials and performance stats."
    }
  ],
  contact: {
    email: "ayesha.cse@sathak.edu.in",
    phone: "+91 98765 43210",
    linkedIn: "https://linkedin.com/in/example-student",
    github: "https://github.com/example-student",
    portfolio: "https://example-student.dev"
  }
};
