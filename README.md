# React & JSX - Practical Foundation Workspace

Hands-on repository for engineering students covering React, Single Page Application (SPA) architecture, JSX syntax, component creation, and practical campus dashboard development.

---

## Workspace Structure

Every module folder contains:
- `notes/`: Terminologies, core concepts, and architecture explanations.
- `programs/`: **Complete, standalone, runnable source code** (ready to run directly in the browser or via Node/Vite).
- `exercises/`: Hands-on coding exercises and engineering challenge tasks.

---

## Curriculum Modules

1. **`01-introduction-to-react-and-spa/`**
   - **Concepts:** Single Page Application (SPA) vs Multi-Page Application (MPA), client-side routing.
   - **Programs:** `spa-demo.html` (complete standalone runnable SPA simulation), `spa-demo-practice.js`.
   - **Exercises:** Dynamic routing challenge adding a campus placement view.

2. **`02-react-vs-traditional-web-development/`**
   - **Concepts:** Imperative DOM manipulation vs Declarative React UI, Virtual DOM & reconciliation.
   - **Programs:** `vanilla-counter.html` (runnable DOM counter), `react-counter.html` (runnable React counter), `react-counter.jsx`.
   - **Exercises:** Refactor imperative visibility toggle to declarative React state.

3. **`03-nodejs-and-npm-setup/`**
   - **Concepts:** Node.js V8 runtime, npm package ecosystem, dependencies vs devDependencies.
   - **Programs:** `node-demo.js` (complete runnable script: `node node-demo.js`), `terminal-commands.txt`.
   - **Exercises:** Initialize npm package and install production & dev tools.

4. **`04-vite-project-creation/`**
   - **Concepts:** Next-generation build tool, ES Modules, Hot Module Replacement (HMR).
   - **Programs:** `vite-setup-guide.md`, `vite-commands-practice.sh`.
   - **Exercises:** Customize Vite server port, document title, and observe instant HMR.

5. **`05-understanding-project-structure/`**
   - **Concepts:** Anatomy of `index.html`, `src/main.jsx`, `createRoot()`, and `App.jsx`.
   - **Programs:** `root-render-demo.html` (standalone mount demo), `root-render-practice.jsx`.
   - **Exercises:** Build modular layout with `<AppHeader />` and `<AppFooter />`.

6. **`06-jsx-syntax-and-expressions/`**
   - **Concepts:** JSX rules, curly brace `{}` expressions, `className`, self-closing tags, ternary operators.
   - **Programs:** `jsx-syntax-demo.html` (standalone live JSX demo), `jsx-syntax-practice.jsx`.
   - **Exercises:** Fix broken JSX syntax and calculate exam pass percentages dynamically.

7. **`07-functional-components/`**
   - **Concepts:** Functions as UI components, props, PascalCase conventions, component composition.
   - **Programs:** `functional-components-demo.html` (standalone composition demo), `functional-components-practice.jsx`.
   - **Exercises:** Build composable department badges, status pills, and student directory cards.

8. **`08-component-rendering/`**
   - **Concepts:** Rendering arrays with `.map()`, mandatory unique `key` prop, list diffing.
   - **Programs:** `list-rendering-demo.html` (standalone table rendering), `list-rendering-practice.jsx`.
   - **Exercises:** Render course grade report with pass/arrear conditional badges.

9. **`09-practical-student-profile-dashboard/`**
   - **Concepts:** Full dashboard composition, profile avatar, academic metrics, skills, and contact links.
   - **Programs:** `student-dashboard/index.html` (complete runnable dashboard), `StudentProfileDashboard.jsx`, `student-data.js`.
   - **Exercises:** Add standing arrears warning alert, SGPA history, and skill filtering.

10. **`10-placement-focus/`**
    - **Concepts:** Campus recruitment technical interview coding questions and rapid-fire concepts.
    - **Programs:** `interview-coding-demo.html` (runnable live interview challenges), `interview-coding-practice.jsx`.
    - **Exercises:** 60-second mock technical interview drill covering React fundamentals.

---

## How to Run the Programs

- **Method 1: Standalone Direct Browser Run (Instant, No Setup Required)**
  - Open any `.html` file inside `programs/` (e.g. `programs/spa-demo.html` or `programs/student-dashboard/index.html`) by double-clicking it in your file explorer or right-clicking and selecting **Open with Chrome / Edge**.
- **Method 2: Node.js Terminal Execution**
  - Run Node scripts directly in terminal: `node <path-to-script>.js`.
- **Method 3: Inside a Vite Project**
  - Import the `.jsx` component files directly into your Vite `src/` directory.
