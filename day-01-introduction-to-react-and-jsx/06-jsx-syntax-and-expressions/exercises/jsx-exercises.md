# 🏋️ Practice Exercises: JSX Syntax & Expressions

Try solving these mini-challenges directly in your scratchpad or a test component.

---

### Challenge 1: Fix the Broken JSX
Find and fix all 4 syntax errors in this snippet:
```jsx
// ❌ BROKEN CODE:
function BrokenComponent() {
  return (
    <h2 class="heading">Welcome to Mohammed Sathak
    <img src="avatar.jpg">
    <p>Current Year: {new Date().getFullYear()}<p>
    <input type="text" placeholder="Enter name">
  );
}
```

#### Your Fixed Code:
<!-- Write your corrected JSX below -->


---

### Challenge 2: Dynamic Greeting Expression
Create a JSX expression that:
- Reads a variable `hours = new Date().getHours()`.
- Dynamically displays:
  - `"Good Morning"` if `hours < 12`
  - `"Good Afternoon"` if `hours >= 12 && hours < 17`
  - `"Good Evening"` otherwise.

#### Your Solution:
<!-- Write your solution below -->


---

### Challenge 3: Student Badge with Conditional Rendering
Given:
```javascript
const student = {
  name: "Zainab",
  department: "Computer Science",
  attendance: 88,
  cgpa: 8.9
};
```
Render a student card in JSX that shows:
1. Student name inside `<h2>`.
2. Department inside `<p>`.
3. If `attendance >= 75`, render `<span className="badge-green">Eligible for Exams</span>`. Otherwise, render `<span className="badge-red">Shortage of Attendance</span>`.
4. If `cgpa >= 8.5`, render `<span className="badge-gold">⭐ Distinction Student</span>`.

#### Your Solution:
<!-- Write your solution below -->
