/**
 * Practical: Simulating a Single Page Application (SPA) vs Multi-Page Navigation
 * 
 * In traditional Multi-Page Applications (MPAs), clicking a link requests a brand new
 * HTML file from the server, causing a full page reload (white flash, slow).
 * 
 * In an SPA (like React), JavaScript dynamically switches the view inside a single root
 * container without reloading the page.
 */

// Simulated component views
const views = {
  home: "<h1>Home View</h1><p>Welcome to Campus Student Portal</p>",
  profile: "<h1>Profile View</h1><p>Name: Alex Morgan | Dept: CSE</p>",
  courses: "<h1>Courses View</h1><p>Enrolled: React.js & Web Development</p>",
  grades: "<h1>Grades View</h1><p>CGPA: 8.85 | Status: All Cleared</p>"
};

// Function to switch view inside the single container (SPA concept)
function navigateTo(page) {
  const root = document.getElementById("root-view") || document.getElementById("root");
  if (root && views[page]) {
    root.innerHTML = views[page];
    console.log(`[SPA Event] Navigated to: ${page} (Zero full page reloads)`);
  } else {
    console.warn(`View "${page}" not found in views dictionary.`);
  }
}

// Export for module usage or testing
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { views, navigateTo };
}
