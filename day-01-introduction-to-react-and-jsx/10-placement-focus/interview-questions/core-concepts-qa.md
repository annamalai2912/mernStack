# 💼 Core Technical Placement Q&A: Day 1 Concepts

---

### Q1: What is React and is it a library or a framework?
**Answer:**  
React is an open-source **JavaScript library** for building user interfaces, developed and maintained by Meta (Facebook).  
- It is a **library** (not a framework) because it focuses solely on the View layer of MVC. Developers have the freedom to choose their own routing (React Router), state management (Redux, Zustand), and build tools. In contrast, frameworks like Angular dictate the complete architecture.

---

### Q2: What is a Single Page Application (SPA) and how does it differ from a Multi-Page Application (MPA)?
**Answer:**  
In an SPA, the browser loads a single HTML file (`index.html`) on the initial visit. As the user navigates, JavaScript dynamically rewrites the DOM by fetching data (via JSON APIs) without triggering a full page reload or white screen flash.  
In an MPA, every link click or form submission sends a new HTTP request to the server, which responds with a completely rendered HTML page, reloading the entire window.

---

### Q3: What is the Virtual DOM and how does React update the UI?
**Answer:**  
The Virtual DOM (VDOM) is a lightweight, in-memory JavaScript object representation of the Real DOM.  
When state or props change:
1. React generates a new Virtual DOM tree.
2. It compares the new VDOM with the snapshot of the previous VDOM (this process is called **Diffing** using an $O(n)$ heuristic algorithm).
3. React calculates the minimum required changes and updates ONLY those specific nodes in the Real DOM (called **Reconciliation** and batching).  
This avoids costly browser reflows and repaints.

---

### Q4: Can browsers read JSX directly? Why or why not?
**Answer:**  
**No.** Browsers only understand standard JavaScript (ECMAScript), HTML, and CSS.  
JSX is not valid JavaScript. A transpiler (such as Babel, esbuild, or SWC) must compile JSX into standard `React.createElement()` function calls before running in the browser.

---

### Q5: Why must component names start with an uppercase letter?
**Answer:**  
In JSX, lowercase tag names (e.g., `<div>`, `<span>`, `<button>`) are treated as built-in HTML elements.  
Uppercase tag names (e.g., `<ProfileCard />`, `<Header />`) signal to the JSX compiler that this is a custom React component reference that needs to be invoked.

---

### Q6: Why do we use `className` instead of `class` in JSX?
**Answer:**  
JSX compiles into standard JavaScript function calls. In JavaScript, `class` is a reserved keyword used for defining ES6 classes. Therefore, React uses `className` to specify HTML class attributes and avoid naming collisions with JS syntax.

---

### Q7: Why is a `key` prop required when rendering lists in React? What happens if you use the array index as the key?
**Answer:**  
Keys provide a stable identity to list elements across renders. They allow React to determine which items were added, modified, or removed during the diffing process.  
- Using array `index` as a key can cause visual bugs, incorrect state mapping, and performance drops if the list is ever filtered, sorted, or mutated. Stable IDs (e.g. database ID) should always be used.

---

### Q8: What is a React Fragment (`<> ... </>`) and why do we use it?
**Answer:**  
Every React component must return a single root element. If you wrap sibling tags in an extra `<div>`, you introduce unnecessary nodes into the DOM tree (DOM bloat), which can break CSS layouts (like flexbox/grid) or semantic HTML (like `<tr>` inside `<table>`).  
A React Fragment allows grouping children without adding any extra node to the real DOM.

---

### Q9: Why did Vite replace Create React App (CRA)?
**Answer:**  
Create React App relies on Webpack, which bundles the entire application code upfront before starting the dev server. As the app grows, server start and reload times become sluggish.  
Vite uses native ES Modules (ESM) in modern browsers to serve source code on-demand and uses `esbuild` (written in Go) for pre-bundling dependencies, resulting in sub-second server startup and instant Hot Module Replacement (HMR).

---

### Q10: What is the difference between Imperative and Declarative programming?
**Answer:**  
- **Imperative (e.g. Vanilla JS):** You write explicit step-by-step instructions telling the computer *how* to achieve the result (e.g. `document.createElement`, `appendChild`).  
- **Declarative (e.g. React):** You describe *what* the UI should look like for a given state ($UI = f(State)$), and React handles the underlying DOM manipulation.
