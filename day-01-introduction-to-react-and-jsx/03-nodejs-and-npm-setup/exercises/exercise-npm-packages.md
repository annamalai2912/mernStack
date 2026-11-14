# Hands-on Exercise: Node.js & npm Package Management

### Objective:
Practice using npm (Node Package Manager) to initialize a Node project, install dependencies, and inspect `package.json`.

---

### Step-by-Step Challenge:

1. **Test Node.js Execution:**
   - In your VS Code terminal, run:
     ```bash
     node ../programs/node-demo.js
     ```
   - Observe the output printed directly to the console.

2. **Initialize a Test Project:**
   - Create and navigate to a new temporary folder:
     ```bash
     mkdir npm-lab-test
     cd npm-lab-test
     npm init -y
     ```
   - Notice the generated `package.json` file.

3. **Install Dependencies:**
   - Install a production dependency:
     ```bash
     npm install canvas-confetti
     ```
   - Install a development tool (`-D` flag):
     ```bash
     npm install -D vite
     ```

4. **Verify package.json Structure:**
   - Open `package.json` and verify:
     - Is `canvas-confetti` placed under `"dependencies"`?
     - Is `vite` placed under `"devDependencies"`?
     - Why are development tools separated from production dependencies?

5. **Test Node Modules Rehydration:**
   - Delete the `node_modules` folder.
   - Run `npm install`.
   - Observe how npm swiftly restores every dependency by reading `package.json` and `package-lock.json`!
