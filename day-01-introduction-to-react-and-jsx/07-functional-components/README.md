# 📌 Module 07: Functional Components

## 🎯 Learning Objectives
By the end of this module, you should be able to:
1. Define what a **React Component** is.
2. Differentiate between Functional Components and legacy Class Components.
3. Understand the rules of naming and structure (PascalCase).
4. Master component exports and imports (Default vs Named).
5. Build modular, reusable UI building blocks.

---

## 📖 Key Concepts

### 1. What is a Component?
- A component is an independent, reusable piece of user interface.
- Think of components like **LEGO bricks**: you build small pieces (Button, Avatar, Card, Navbar) and combine them to create complex applications.
- Components accept inputs (props) and return React elements describing what should appear on the screen.

### 2. Anatomy of a Functional Component
A React functional component is simply a JavaScript function that:
1. Has a name starting with an **uppercase letter** (`PascalCase`).
2. Returns **JSX markup**.

```jsx
// Standard function declaration
function WelcomeBanner() {
  return <h1>Welcome to Day 1 React Training!</h1>;
}

// Arrow function syntax
const WelcomeBanner = () => {
  return <h1>Welcome to Day 1 React Training!</h1>;
};
```

> ⚠️ **CRITICAL RULE:** Component names MUST start with a capital letter (e.g., `ProfileCard`, not `profileCard`). React treats lowercase tags as built-in HTML tags (`<div>`, `<span>`, `<p>`).

### 3. Exporting & Importing Components

#### Option A: Default Export (One per file)
```jsx
// Header.jsx
export default function Header() {
  return <header>College Portal</header>;
}

// App.jsx
import Header from './Header';
```

#### Option B: Named Export (Multiple per file)
```jsx
// Buttons.jsx
export function PrimaryButton() {
  return <button className="btn-primary">Submit</button>;
}

export function SecondaryButton() {
  return <button className="btn-secondary">Cancel</button>;
}

// App.jsx
import { PrimaryButton, SecondaryButton } from './Buttons';
```

---

## ✍️ Student Action Items
1. Complete the challenges in [`exercises/component-exercises.md`](./exercises/component-exercises.md).
2. Review [`code-snippets/component-examples.jsx`](./code-snippets/component-examples.jsx).
3. Fill in your notes in [`notes/learning-notes.md`](./notes/learning-notes.md).
