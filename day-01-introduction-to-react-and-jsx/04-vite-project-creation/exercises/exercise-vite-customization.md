# Hands-on Exercise: Customizing Your Vite React Project

### Objective:
Learn how to customize the core HTML entry point, configure Vite dev server options, and observe instant Hot Module Replacement (HMR).

---

### Step-by-Step Tasks:

1. **Customize Application Title & Brand:**
   - In your Vite project root, open `index.html`.
   - Update the `<title>` tag:
     ```html
     <title>Campus Student Portal</title>
     ```
   - Update the favicon link or add a meta description tag:
     ```html
     <meta name="description" content="College Student Academic & Placement Portal" />
     ```

2. **Configure Vite Dev Server Port (vite.config.js):**
   - Open `vite.config.js` and specify a dedicated port:
     ```javascript
     import { defineConfig } from 'vite';
     import react from '@vitejs/plugin-react';

     export default defineConfig({
       plugins: [react()],
       server: {
         port: 3000,
         open: true // Automatically launches default browser on start
       }
     });
     ```

3. **Launch Dev Server:**
   - In terminal run:
     ```bash
     npm run dev
     ```
   - Notice that the server starts on `http://localhost:3000/` and opens the browser automatically.

4. **Experience Hot Module Replacement (HMR):**
   - Keep the browser open alongside VS Code.
   - Edit `src/App.jsx` and change the main heading text to `"Welcome to Engineering Campus Portal"`.
   - Press `Ctrl + S` to save.
   - Observe how the browser updates **instantly** without reloading the page or losing current component state!
