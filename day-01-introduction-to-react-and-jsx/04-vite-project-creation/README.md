# 📌 Module 04: Vite Project Creation

## 🎯 Learning Objectives
By the end of this module, you should be able to:
1. Explain what **Vite** is and why it has replaced Create React App (CRA).
2. Understand native ES modules (ESM) and esbuild compilation.
3. Scaffold a brand-new React application using the Vite CLI.
4. Start, view, and stop the local development server.

---

## 📖 Key Concepts

### 1. What is Vite?
- **Vite** (French word for "fast", pronounced `/vit/`) is a next-generation frontend build tool created by Evan You (creator of Vue.js).
- **Why is Vite so fast?**
  - **Dev Server:** Leverages native ES Modules (ESM) in modern browsers, serving code on-demand without bundling the entire app upfront.
  - **Pre-bundling:** Uses `esbuild` written in Go, which is 10-100x faster than traditional JS-based bundlers (like Webpack).
  - **Instant Hot Module Replacement (HMR):** Updates only modified components without losing application state.

### 2. Vite vs Create React App (CRA)
| Feature | Vite | Create React App (CRA - Deprecated) |
| :--- | :--- | :--- |
| **Bundler / Tool** | esbuild (dev) + Rollup (prod) | Webpack |
| **Server Start Time** | Milliseconds (< 300ms) | Several seconds to minutes |
| **Hot Module Reloading (HMR)** | Instantaneous | Slower as app size grows |
| **Configuration** | Minimal & highly extensible (`vite.config.js`) | Complex / Requires `react-app-rewired` or `eject` |

### 3. Step-by-Step Project Creation
```bash
# 1. Run the interactive Vite project generator
npm create vite@latest my-react-app -- --template react

# 2. Navigate into the new project folder
cd my-react-app

# 3. Install project dependencies
npm install

# 4. Start the development server
npm run dev
```
Open your browser at the URL shown in terminal (usually `http://localhost:5173/`).

---

## ✍️ Student Action Items
1. Follow the steps above to create your test app inside [`vite-demo-app/`](./vite-demo-app/).
2. Verify that the Vite + React welcome page renders in your browser.
3. Fill in your notes in [`notes/learning-notes.md`](./notes/learning-notes.md).
