# 🛠️ Day 1 Practical Project: Student Profile Dashboard

## 🎯 Project Overview
As the practical assignment for **Day 1**, you will build a clean, responsive **Student Profile Dashboard** using React and JSX. The dashboard will showcase student details, profile photo/avatar, academic stats, technical skills, and contact links using modular functional components.

---

## 🏗️ Component Architecture
Your application should be broken down into clean, single-responsibility components:

```text
App (Root Component)
 └── DashboardLayout (Container with navigation/header)
      ├── Header (Institution logo, title, theme indicator)
      ├── ProfileCard (Avatar, Name, Roll No, Department, Year, Bio)
      ├── AcademicStats (Semester GPA, Overall CGPA, Attendance %)
      ├── SkillsSection (Skill badges rendered dynamically using .map)
      ├── ProjectsList (Cards showing student mini-projects)
      └── ContactCard (Email, Phone, LinkedIn, GitHub links)
```

---

## 🎨 Recommended UI Layout / Wireframe
```text
+---------------------------------------------------------------+
|  [Logo] MOHAMMED SATHAK - STUDENT PORTAL           [Profile]   |
+---------------------------------------------------------------+
|  +------------------------+  +------------------------------+ |
|  |      PROFILE CARD      |  |        ACADEMIC STATS        | |
|  |  [ Avatar / Photo ]    |  |  CGPA: 8.9  | Attendance: 92%| |
|  |  Name: Student Name    |  |  Status: Eligible for Plcmt | |
|  |  Dept: B.Tech CSE      |  +------------------------------+ |
|  |  Roll No: 911521104... |  |      TECHNICAL SKILLS        | |
|  |  Batch: 2022 - 2026    |  |  [React] [JS] [HTML] [CSS]   | |
|  +------------------------+  +------------------------------+ |
|  |     PROJECTS CARDS     |  |       CONTACT & SOCIALS      | |
|  |  - E-Commerce UI       |  |  Email: student@sathak.edu   | |
|  |  - Portfolio Website   |  |  GitHub: github.com/...      | |
|  +------------------------+  +------------------------------+ |
+---------------------------------------------------------------+
```

---

## ✅ Acceptance Criteria (Checklist for Students)
- [ ] Project initialized cleanly with **Vite** (`npm create vite@latest . -- --template react`).
- [ ] At least **5 separate functional components** created and composed inside `App.jsx`.
- [ ] Proper use of **JSX expressions** (`{}`) for all dynamic data.
- [ ] All tags properly closed and proper attribute names used (`className`, `htmlFor`).
- [ ] At least one dynamic list (e.g. skills or projects) rendered using `.map()` with a unique `key`.
- [ ] Conditional rendering used (e.g. attendance badge color, placement eligibility tag).
- [ ] Clean and visually appealing CSS styling (either standard CSS in `App.css` or Tailwind/inline styles).
- [ ] Running without console errors or JSX syntax warnings.

---

## 🚀 Step-by-Step Instructions
1. Navigate into `student-solution/`:
   ```bash
   cd "day-01-introduction-to-react-and-jsx/09-practical-student-profile-dashboard/student-solution"
   ```
2. Initialize your Vite React application:
   ```bash
   npm create vite@latest . -- --template react
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. Copy the sample data from [`../starter-template/student-data.js`](./starter-template/student-data.js) into your `src/` folder.
5. Create your components inside a `src/components/` folder:
   - `src/components/Header.jsx`
   - `src/components/ProfileCard.jsx`
   - `src/components/AcademicStats.jsx`
   - `src/components/SkillsSection.jsx`
   - `src/components/ContactCard.jsx`
6. Import and assemble them inside `src/App.jsx`.
7. Start your server and test:
   ```bash
   npm run dev
   ```
8. Take a screenshot of your working dashboard and save it in [`screenshots/`](./screenshots/).
