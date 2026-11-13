# 📌 Module 06: JSX Syntax and Expressions

## 🎯 Learning Objectives
By the end of this module, you should be able to:
1. Explain what **JSX** is and why React uses it.
2. Understand that JSX is syntactic sugar for `React.createElement()`.
3. Follow the strict syntactic rules of JSX.
4. Embed JavaScript expressions, variables, and calculations using curly braces `{}`.
5. Use conditional rendering techniques inside JSX.

---

## 📖 Key Concepts

### 1. What is JSX?
- **JSX** stands for **JavaScript XML**.
- It is a syntax extension for JavaScript that looks like HTML.
- It allows you to write HTML-like markup directly inside JavaScript files.
- Under the hood, JSX is compiled by Babel/esbuild into pure JavaScript function calls:
  ```jsx
  // What you write (JSX):
  const element = <h1 className="title">Hello World</h1>;

  // What it compiles to (Pure JS):
  const element = React.createElement('h1', { className: 'title' }, 'Hello World');
  ```

### 2. Core Rules of JSX
1. **Single Root Element:** Every component must return a single top-level tag. Wrap multiple siblings in a parent `<div>` or a **React Fragment** (`<> ... </>`).
2. **Close All Tags:** All tags must be explicitly closed, including void elements (`<img />`, `<input />`, `<br />`, `<hr />`).
3. **`camelCase` Attribute Naming:**
   - Use `className` instead of `class` (since `class` is a reserved keyword in JS).
   - Use `htmlFor` instead of `for`.
   - Event handlers: `onClick`, `onChange`, `onSubmit`.
4. **Embedding JS Expressions:** Use single curly braces `{expression}`:
   ```jsx
   const studentName = "Amina";
   const marks = 85;
   return <h3>{studentName}'s Score: {marks * 1.1}%</h3>;
   ```
5. **Inline Styles as Objects:** Style attribute takes a JavaScript object with camelCase keys:
   ```jsx
   <div style={{ color: 'white', backgroundColor: '#0055ff', padding: '12px' }}>
     Styled Card
   </div>
   ```

### 3. Conditional Rendering in JSX
- **Ternary Operator (`condition ? A : B`):**
  ```jsx
  <p>Status: {isPassed ? "Congratulations! Passed" : "Needs Improvement"}</p>
  ```
- **Logical AND (`condition && A`):**
  ```jsx
  {hasScholarship && <span className="badge">Scholarship Holder</span>}
  ```

---

## ✍️ Student Action Items
1. Try out the practice problems in [`exercises/jsx-exercises.md`](./exercises/jsx-exercises.md).
2. Review [`code-snippets/jsx-cheat-sheet.jsx`](./code-snippets/jsx-cheat-sheet.jsx).
3. Fill in your notes in [`notes/learning-notes.md`](./notes/learning-notes.md).
