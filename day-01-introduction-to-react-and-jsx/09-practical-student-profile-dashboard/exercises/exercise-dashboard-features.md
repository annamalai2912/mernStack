# Hands-on Exercise: Student Profile Dashboard Enhancements

### Objective:
Extend the working Student Profile Dashboard with dynamic conditional logic and college-focused data features.

---

### Prerequisites:
Run and inspect `../programs/student-dashboard/index.html` in your browser. Verify the profile header, academic stats, skills, and contact links.

---

### Step-by-Step Feature Tasks:

1. **Task 1: Standing Arrears Warning Banner**
   - In `AcademicStats`, check if `academics.standingArrears > 0`:
     - If arrears > 0, render a prominent warning banner:
       ```jsx
       <div style={{ background: '#fef2f2', border: '1px solid #f87171', color: '#991b1b', padding: '10px', borderRadius: '6px', marginTop: '14px' }}>
         ⚠️ Academic Advisory: {academics.standingArrears} active arrear(s) pending clearance.
       </div>
       ```
     - If arrears === 0, render a success badge: `✨ Clean Academic Record (0 Arrears)`.

2. **Task 2: Add Semester SGPA Breakdown Table**
   - In `student-data.js`, add a semester grade history array:
     ```javascript
     semesterScores: [
       { sem: "Sem 1", gpa: 8.5 },
       { sem: "Sem 2", gpa: 8.7 },
       { sem: "Sem 3", gpa: 8.9 },
       { sem: "Sem 4", gpa: 9.1 },
       { sem: "Sem 5", gpa: 8.8 }
     ]
     ```
   - Render these semester scores as a clean list or row using `.map()` with `key={item.sem}`.

3. **Task 3: Add Skills Category Filtering**
   - Add a prop or local state to filter skills (e.g., all skills vs. frontend skills vs. core tools).
   - Display a counter badge showing: `Total Core Skills: {skills.length}`.

4. **Task 4: Add Direct Telephone Dial Action**
   - Add a phone number in `contact`: `phone: "+91 98765 43210"`.
   - Render a callable action link: `<a href={"tel:" + contact.phone}>📞 Call Direct</a>`.
