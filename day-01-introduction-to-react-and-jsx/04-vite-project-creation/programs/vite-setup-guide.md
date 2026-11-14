# Vite React Project Setup Guide

### Step 1: Create a New Vite React Project
Run in your terminal (PowerShell, Command Prompt, or Bash):
```bash
npm create vite@latest student-portal -- --template react
```

### Step 2: Navigate into the Project Folder
```bash
cd student-portal
```

### Step 3: Install Required Dependencies
```bash
npm install
```

### Step 4: Start the Local Development Server
```bash
npm run dev
```

### Step 5: Open in Browser
Visit the printed local URL (typically `http://localhost:5173/` or `http://localhost:3000/`).

---

### Key Project Files Created:
- `index.html`: The single HTML shell containing `<div id="root"></div>`
- `src/main.jsx`: The React mount entry point using `ReactDOM.createRoot`
- `src/App.jsx`: The root component displaying the initial UI
- `package.json`: Project metadata, dependencies, and build scripts (`dev`, `build`, `preview`)
