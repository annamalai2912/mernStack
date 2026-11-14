# Practical Exercise: Student Profile Dashboard Enhancements

After building the base dashboard inside `../programs/student-dashboard/`:

### Feature Challenges to Complete:
1. **Attendance Warning Alert:**
   - If `studentData.academics.attendance < 75`, render a prominent red alert banner:  
     `⚠️ Warning: Attendance is below 75%. Not eligible for semester examinations.`
   - If attendance >= 75%, render a green badge: `✅ Examination Eligible`.

2. **Placement Eligibility Pill:**
   - Inspect `studentData.academics.isPlacementEligible`.
   - Conditionally render a star badge: `⭐ Registered for Campus Placements`.

3. **Dynamic Skills Count:**
   - Add a counter badge inside the Skills header showing: `Total Skills: {studentData.skills.length}`.

4. **Contact Action Buttons:**
   - Render functional mailto and tel links:
     - `<a href={"mailto:" + studentData.contact.email}>Send Email</a>`
     - `<a href={"tel:" + studentData.contact.phone}>Call</a>`

