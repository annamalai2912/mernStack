# 🚀 React & Frontend Engineering Bootcamp
## 📅 DAY 1: Introduction to React & JSX (6 Hours)

Welcome to **Day 1** of the React Training Program at **Mohammed Sathak**! This repository is your structured personal workspace for Day 1. It is designed to help you take notes, complete exercises, build your hands-on dashboard project, and prepare for campus placement technical interviews.

---

## 📌 Day 1 Curriculum Overview (6 Hours)

| Module | Topic | Description & Key Focus | Folder |
| :---: | :--- | :--- | :--- |
| **01** | **Introduction to React & SPA** | React history, Component-driven architecture, Single Page Application (SPA) vs Multi-Page Application (MPA) | [`01-introduction-to-react-and-spa`](./day-01-introduction-to-react-and-jsx/01-introduction-to-react-and-spa/) |
| **02** | **React vs Traditional Web Development** | DOM vs Virtual DOM, Imperative vs Declarative UI, Reconciliation & Diffing algorithm | [`02-react-vs-traditional-web-development`](./day-01-introduction-to-react-and-jsx/02-react-vs-traditional-web-development/) |
| **03** | **Node.js & npm Setup** | Node runtime, npm CLI, `package.json`, dependencies vs devDependencies, semantic versioning | [`03-nodejs-and-npm-setup`](./day-01-introduction-to-react-and-jsx/03-nodejs-and-npm-setup/) |
| **04** | **Vite Project Creation** | Why Vite over CRA, bundling with esbuild, creating a project with `npm create vite@latest` | [`04-vite-project-creation`](./day-01-introduction-to-react-and-jsx/04-vite-project-creation/) |
| **05** | **Understanding Project Structure** | `index.html`, `src/main.jsx`, `createRoot`, `App.jsx`, assets, CSS styling, configuration files | [`05-understanding-project-structure`](./day-01-introduction-to-react-and-jsx/05-understanding-project-structure/) |
| **06** | **JSX Syntax & Expressions** | What is JSX, embedding JS `{expression}`, JSX rules, React Fragments (`<>`), styling & attributes | [`06-jsx-syntax-and-expressions`](./day-01-introduction-to-react-and-jsx/06-jsx-syntax-and-expressions/) |
| **07** | **Functional Components** | Anatomy of a component, PascalCase naming, returning JSX, default vs named exports, modularity | [`07-functional-components`](./day-01-introduction-to-react-and-jsx/07-functional-components/) |
| **08** | **Component Rendering** | Rendering pipeline, component hierarchy (Parent & Child), rendering lists with `.map()`, `key` prop | [`08-component-rendering`](./day-01-introduction-to-react-and-jsx/08-component-rendering/) |
| **09** | **Practical: Student Profile Dashboard** | Hands-on project: Build a modular student dashboard using reusable functional components | [`09-practical-student-profile-dashboard`](./day-01-introduction-to-react-and-jsx/09-practical-student-profile-dashboard/) |
| **10** | **Placement Focus & Interview Prep** | Campus recruitment Q&A: React core concepts, SPA mechanics, JSX under the hood, VDOM interview questions | [`10-placement-focus`](./day-01-introduction-to-react-and-jsx/10-placement-focus/) |

---

## 📂 Repository Directory Structure

```text
mohammed-sathak/
├── .gitignore
├── README.md                                          <-- Master Guide (You are here)
└── day-01-introduction-to-react-and-jsx/
    ├── 01-introduction-to-react-and-spa/
    │   ├── README.md                                  <-- Module concepts & theory
    │   ├── notes/                                     <-- Your notes & summaries
    │   └── resources/                                 <-- Articles, links & diagrams
    ├── 02-react-vs-traditional-web-development/
    │   ├── README.md
    │   ├── notes/
    │   └── comparison-code/                           <-- DOM vs React code samples
    ├── 03-nodejs-and-npm-setup/
    │   ├── README.md
    │   ├── notes/
    │   └── commands-cheatsheet/                       <-- npm commands reference
    ├── 04-vite-project-creation/
    │   ├── README.md
    │   ├── notes/
    │   └── vite-demo-app/                             <-- Test Vite sandbox
    ├── 05-understanding-project-structure/
    │   ├── README.md
    │   ├── notes/
    │   └── diagrams-and-flowcharts/                   <-- Project tree & workflow diagrams
    ├── 06-jsx-syntax-and-expressions/
    │   ├── README.md
    │   ├── notes/
    │   ├── exercises/                                 <-- Practice exercises
    │   └── code-snippets/                             <-- Saved JSX snippets
    ├── 07-functional-components/
    │   ├── README.md
    │   ├── notes/
    │   ├── exercises/
    │   └── code-snippets/
    ├── 08-component-rendering/
    │   ├── README.md
    │   ├── notes/
    │   ├── exercises/
    │   └── code-snippets/
    ├── 09-practical-student-profile-dashboard/
    │   ├── README.md                                  <-- Practical specifications & guide
    │   ├── starter-template/                          <-- Starter boilerplates & assets
    │   ├── student-solution/                          <-- YOUR PROJECT GOES HERE!
    │   └── screenshots/                               <-- UI output screenshots
    └── 10-placement-focus/
        ├── README.md                                  <-- Placement orientation
        ├── interview-questions/                       <-- Top technical interview Q&A
        ├── student-answers/                           <-- Write your own answers for practice
        └── flashcards-and-cheatsheet/                 <-- Rapid revision cheat sheet
```

---

## 🛠️ Student Workflow & Getting Started

### 1. Clone the Repository
Open your terminal (Git Bash, Command Prompt, or PowerShell) and run:
```bash
git clone <YOUR_REPO_URL>
cd "mohammed sathak"
```

### 2. Create Your Personal Branch (Recommended)
Work on your own branch to avoid conflicts:
```bash
git checkout -b student/<your-name>-day-01
# Example: git checkout -b student/mohammed-day-01
```

### 3. As You Learn During the 6-Hour Session:
- Fill out the `learning-notes.md` templates in each folder's `notes/` directory.
- Complete the mini exercises in each module's `exercises/` folder.
- Save your code snippets in `code-snippets/`.

### 4. Build the Practical Project:
- Navigate to `day-01-introduction-to-react-and-jsx/09-practical-student-profile-dashboard/student-solution/`.
- Initialize your Vite app:
  ```bash
  npm create vite@latest . -- --template react
  npm install
  npm run dev
  ```
- Build your **Student Profile Dashboard** components.
- Take a screenshot of your dashboard and place it in the `screenshots/` directory.

### 5. Review Placement Material:
- Open `10-placement-focus/interview-questions/core-concepts-qa.md` to review the most common fresher interview questions on Day 1 topics.
- Write your own technical answers in `10-placement-focus/student-answers/my-interview-prep.md`.

### 6. Commit & Push Your Work:
```bash
git add .
git commit -m "feat(day-01): completed notes, exercises, and student dashboard"
git push origin student/<your-name>-day-01
```

---

## 💡 Important Git Note for Students
> **Why do these folders have `.gitkeep` files?**  
> Git does not track completely empty directories. To ensure that the full folder structure exists on your computer when you clone this repository, each folder includes a small `.gitkeep` placeholder or a template markdown file. When you add your code or notes, you can keep or replace them!

---

⭐ **Happy Coding & Welcome to React!**
