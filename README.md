# React & JSX - Practical Foundation Workspace

Hands-on repository for engineering students covering React, Single Page Application (SPA) architecture, JSX syntax, component creation, and practical campus dashboard development.

---

## Workspace Structure

Every module folder contains:
- `notes/`: Terminologies, core concepts, and architecture explanations.
- `programs/`: **Simple, complete, runnable source code** (short, minimal examples).
- `exercises/`: Hands-on coding exercises and engineering challenge tasks.

---

## Curriculum Modules

1. **`01-introduction-to-react-and-spa/`**
   - **Concepts:** Single Page Application (SPA) vs Multi-Page Application (MPA).
   - **Programs:** `spa-demo.html` (runnable SPA demo, open directly in browser).
   - **Exercises:** `exercise-spa-concept.md` (add a new view).

2. **`02-react-vs-traditional-web-development/`**
   - **Concepts:** Imperative DOM manipulation vs Declarative React UI.
   - **Programs:** `vanilla-counter.html` (DOM counter), `react-counter.jsx` (React counter).
   - **Exercises:** `exercise-dom-vs-react.jsx` (add decrement button).

3. **`03-nodejs-and-npm-setup/`**
   - **Concepts:** Node.js runtime and npm package management.
   - **Programs:** `node-demo.js` (run with: `node node-demo.js`), `terminal-commands.txt`.
   - **Exercises:** `exercise-npm-packages.md` (practice npm commands).

4. **`04-vite-project-creation/`**
   - **Concepts:** Vite build tool and Hot Module Replacement (HMR).
   - **Programs:** `vite-setup-guide.md` (4 core setup commands).
   - **Exercises:** `exercise-vite-customization.md` (customize title and heading).

5. **`05-understanding-project-structure/`**
   - **Concepts:** `index.html`, `main.jsx`, `createRoot()`, and `App.jsx`.
   - **Programs:** `root-render-practice.jsx` (mounting component into root).
   - **Exercises:** `exercise-mount-structure.jsx` (add a Footer component).

6. **`06-jsx-syntax-and-expressions/`**
   - **Concepts:** JSX rules, curly braces `{}`, `className`, self-closing tags.
   - **Programs:** `jsx-syntax-practice.jsx` (clean dynamic expressions).
   - **Exercises:** `exercise-jsx-fixes-and-expressions.jsx` (fix 3 syntax bugs).

7. **`07-functional-components/`**
   - **Concepts:** Components as functions, props, and composition.
   - **Programs:** `functional-components-practice.jsx` (reusable StudentCard with props).
   - **Exercises:** `exercise-modular-cards.jsx` (display a CGPA prop).

8. **`08-component-rendering/`**
   - **Concepts:** Rendering lists with `.map()` and unique `key`.
   - **Programs:** `list-rendering-practice.jsx` (clean list rendering).
   - **Exercises:** `exercise-list-rendering.jsx` (render courses array).

9. **`09-practical-student-profile-dashboard/`**
   - **Concepts:** Composing profile details, academic stats, and skills list.
   - **Programs:** `student-data.js` (profile data), `StudentProfileDashboard.jsx` (dashboard component).
   - **Exercises:** `exercise-dashboard-features.md` (add email and new skill).

10. **`10-placement-focus/`**
    - **Concepts:** Campus recruitment technical interview questions.
    - **Programs:** `interview-coding-practice.jsx` (clean state counter).
    - **Exercises:** `exercise-placement-mock-interview.md` (3 core interview Q&As).

---

## How to Run the Programs

- **Browser-Ready Files:** Double-click any `.html` file (e.g. `programs/spa-demo.html`, `programs/vanilla-counter.html`) in your file explorer to open it in Chrome or Edge.
- **Node.js Scripts:** Run `node <filename>.js` in your terminal.
- **React Components:** Copy or import the `.jsx` files into your Vite project's `src/` folder.
