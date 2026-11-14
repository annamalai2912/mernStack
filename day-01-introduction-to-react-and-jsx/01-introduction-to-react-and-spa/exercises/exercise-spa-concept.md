# Hands-on Exercise: SPA View Navigation & Routing

### Objective:
Experience firsthand how Single Page Applications (SPAs) switch views without refreshing the browser, and expand the application with a new campus feature.

---

### Step-by-Step Instructions:

1. **Run the Program:**
   - Locate and double-click `../programs/spa-demo.html` in your browser (Chrome/Edge).
   - Click between **Home**, **Student Profile**, **Enrolled Courses**, and **Semester Grades**.
   - Notice the status bar at the bottom: **Browser Page Reloads** stays at `1`, while **Client View Switches** increments instantly.

2. **Add a New Campus Feature (Placement View):**
   - Open `../programs/spa-demo.html` in VS Code.
   - Inside the `<nav>` section, add a new navigation button:
     ```html
     <button id="btn-placement" onclick="navigateTo('placement')">Placements</button>
     ```
   - In the `<script>` section, add a new view named `placement` inside the `views` object:
     ```javascript
     placement: `
       <h2>Campus Placement Cell</h2>
       <div class="card">
         <p><strong>Eligibility:</strong> CGPA >= 7.5 & 0 Standing Arrears</p>
         <p><strong>Upcoming Drive:</strong> Infosys, Zoho, TCS Digital</p>
         <p style="margin-top: 8px;"><span class="badge">Registration: Open</span></p>
       </div>
     `
     ```

3. **Verify in Browser:**
   - Refresh the page once and click the new **Placements** button.
   - Verify that the new view renders inside the root container without reloading the page.

4. **Self-Check Questions:**
   - What happens to JavaScript variables and application state when a traditional page reloads?
   - Why do modern frameworks like React build applications as SPAs?
