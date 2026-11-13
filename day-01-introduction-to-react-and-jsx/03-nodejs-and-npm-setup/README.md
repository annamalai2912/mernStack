# 📌 Module 03: Node.js and npm Setup

## 🎯 Learning Objectives
By the end of this module, you should be able to:
1. Understand what **Node.js** is and why modern frontend tools require it.
2. Understand what **npm** (Node Package Manager) is and how it manages dependencies.
3. Check and verify environment setup using command-line commands.
4. Understand the purpose of `package.json`, `package-lock.json`, and the `node_modules/` folder.

---

## 📖 Key Concepts

### 1. What is Node.js?
- Node.js is an open-source, cross-platform JavaScript runtime environment built on Chrome's V8 engine.
- Even though React runs in the browser, development tools (like Vite, Webpack, Babel, ESLint, Prettier) run on your local machine using Node.js.

### 2. What is npm?
- npm is the default package manager for Node.js and the world's largest software registry.
- It allows developers to install third-party libraries, manage project scripts, and handle project dependencies.

### 3. Verification Commands
Run these commands in your terminal to verify installation:
```bash
# Check Node.js version (Recommended: v18+ or v20+ LTS)
node -v

# Check npm version
npm -v
```

### 4. Key Project Files Explained
- **`package.json`**: The manifest file of your project. Lists project name, version, scripts (`dev`, `build`, `preview`), and lists of `dependencies` and `devDependencies`.
- **`package-lock.json`**: Records the exact version of every installed package and sub-dependency to ensure consistent builds across machines.
- **`node_modules/`**: Contains the downloaded code of all dependencies. **Never edit this folder manually, and never commit it to Git!**

---

## ✍️ Student Action Items
1. Run `node -v` and `npm -v` in your terminal and record your installed versions.
2. Review the command reference in [`commands-cheatsheet/npm-cheatsheet.md`](./commands-cheatsheet/npm-cheatsheet.md).
3. Fill in your notes in [`notes/learning-notes.md`](./notes/learning-notes.md).
