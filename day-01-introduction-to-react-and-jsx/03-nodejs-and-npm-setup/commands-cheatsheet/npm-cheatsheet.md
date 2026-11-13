# ⚡ Essential npm & Terminal Commands Cheatsheet

### 1. Verification & Information
```bash
node -v                  # Print installed Node.js version
npm -v                   # Print installed npm version
npx --version            # Print npx version
```

### 2. Initializing & Installing
```bash
npm init -y              # Initialize a default package.json
npm install              # Install all dependencies listed in package.json
npm i <package_name>     # Install a production dependency (e.g. npm i lucide-react)
npm i -D <package_name>  # Install a development dependency (e.g. npm i -D tailwindcss)
npm uninstall <package>  # Remove a dependency
```

### 3. Running Scripts
```bash
npm run dev              # Start the local development server (in Vite)
npm run build            # Compile and bundle the app for production
npm run preview          # Preview the production build locally
```

### 4. Clearing Cache / Troubleshooting
```bash
npm cache clean --force  # Force clear npm local cache
rm -rf node_modules package-lock.json # Remove installed packages (Linux/macOS)
Remove-Item -Recurse -Force node_modules, package-lock.json # PowerShell (Windows)
npm install              # Reinstall clean dependencies
```
