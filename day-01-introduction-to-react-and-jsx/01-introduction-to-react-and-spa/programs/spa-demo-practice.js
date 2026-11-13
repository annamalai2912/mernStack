/**
 * Practical: Simulating a Single Page Application (SPA) vs Multi-Page navigation
 * 
 * Practice how an SPA dynamically switches views inside a single root container
 * without requesting a full page reload from the server.
 */

// Simulated views
const views = {
  home: "<h1>Home View</h1><p>Welcome to Mohammed Sathak Student Portal</p>",
  profile: "<h1>Profile View</h1><p>Name: Student | Dept: CSE</p>",
  courses: "<h1>Courses View</h1><p>Enrolled: React.js & Web Development</p>"
};

// Function to switch view inside the single container (SPA concept)
function navigateTo(page) {
  const root = document.getElementById("root");
  if (root && views[page]) {
    root.innerHTML = views[page];
    console.log(`Navigated to: ${page} (No page reload triggered)`);
  }
}

// Student Practice: Try adding a new view (e.g. 'grades') and call navigateTo('grades')
