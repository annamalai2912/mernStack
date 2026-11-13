# Exercise: Customizing Your Vite React Project

### Tasks to Complete:
1. In your generated Vite project:
   - Open `index.html`.
   - Change the `<title>` tag from `"Vite + React"` to `"Mohammed Sathak - Student Portal"`.
2. Open `vite.config.js` and configure the dev server port to `3000`:
   ```javascript
   export default defineConfig({
     plugins: [react()],
     server: {
       port: 3000,
       open: true // Automatically opens browser on npm run dev
     }
   });
   ```
3. Restart your dev server with `npm run dev`.
4. Verify that the app now opens on port 3000 automatically with your new custom title!
