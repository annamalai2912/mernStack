# 📦 Starter Template Resources

This directory contains starter assets and mock data for your **Student Profile Dashboard**.

### Files:
- [`student-data.js`](./student-data.js): Contains a sample student profile object with personal details, academics, skills, projects, and contact info.

### How to Use:
1. When you create your Vite project inside `student-solution/`, copy `student-data.js` into your `src/` folder.
2. In your components (e.g. `ProfileCard.jsx`, `SkillsSection.jsx`), import the data:
   ```jsx
   import { studentProfile } from '../student-data';
   ```
3. Use the data to populate your components dynamically with JSX expressions!
