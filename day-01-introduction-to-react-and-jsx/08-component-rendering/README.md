# 📌 Module 08: Component Rendering

## 🎯 Learning Objectives
By the end of this module, you should be able to:
1. Understand the component rendering lifecycle (Trigger -> Render -> Commit).
2. Master component composition (nesting parent and child components).
3. Render lists and collections dynamically using JavaScript's `.map()` method.
4. Explain why the `key` prop is mandatory when rendering lists in React.

---

## 📖 Key Concepts

### 1. The Rendering Pipeline
1. **Triggering a Render:** Happens on initial load (`createRoot().render()`) or when state/props change.
2. **Rendering the Component:** React calls your functional component to determine what JSX elements should be on screen.
3. **Committing to the DOM:** React calculates the minimum diff and modifies the actual browser DOM.

### 2. Component Composition (Parent & Child)
In React, we build complex UIs by nesting components inside one another:
```jsx
function Dashboard() {
  return (
    <div className="dashboard-container">
      <Header />
      <div className="main-content">
        <Sidebar />
        <StudentProfile />
      </div>
      <Footer />
    </div>
  );
}
```

### 3. Rendering Dynamic Lists with `.map()`
React developers use standard JavaScript array methods, predominantly `.map()`, to transform data arrays into arrays of JSX elements:
```jsx
const subjects = [
  { id: 101, name: "Data Structures", code: "CS8391", credits: 4 },
  { id: 102, name: "Web Technology", code: "IT8401", credits: 3 },
  { id: 103, name: "React & Cloud", code: "MS2024", credits: 3 }
];

function CourseList() {
  return (
    <ul>
      {subjects.map((course) => (
        <li key={course.id}>
          <strong>{course.code}</strong>: {course.name} ({course.credits} Credits)
        </li>
      ))}
    </ul>
  );
}
```

### 4. Why is the `key` Prop Required?
- **Keys give elements a stable identity.**
- When array items are added, deleted, reordered, or modified, React uses the `key` to match items in the new VDOM with items in the old VDOM.
- **Rule of Thumb:**
  - Always use a unique and stable identifier (like `id` from the database/data).
  - ❌ Avoid using array index (`index`) as key if items can be sorted, inserted, or removed, as this causes rendering bugs and performance hits.

---

## ✍️ Student Action Items
1. Complete the challenges in [`exercises/rendering-exercises.md`](./exercises/rendering-exercises.md).
2. Review [`code-snippets/rendering-patterns.jsx`](./code-snippets/rendering-patterns.jsx).
3. Fill in your notes in [`notes/learning-notes.md`](./notes/learning-notes.md).
