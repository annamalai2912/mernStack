# 📌 Module 01: Introduction to React & SPA

## 🎯 Learning Objectives
By the end of this module, you should be able to:
1. Explain what React is and why it was developed by Meta (Facebook).
2. Understand the concept of Single Page Applications (SPA).
3. Differentiate between Single Page Applications (SPA) and Traditional Multi-Page Applications (MPA).
4. Explain client-side rendering (CSR) and how it improves user experience.

---

## 📖 Key Concepts

### 1. What is React?
- React is an **open-source JavaScript library** (not a full-fledged framework) designed for building fast, interactive user interfaces (UIs).
- Developed by Jordan Walke at Facebook (Meta) in 2011 and open-sourced in May 2013.
- Core philosophy: **Component-Based Architecture**, **Declarative UI**, and **Unidirectional Data Flow**.

### 2. What is a Single Page Application (SPA)?
- A **Single Page Application (SPA)** is a web application that loads a single HTML page (`index.html`) on the initial request.
- Subsequent interactions dynamically update the existing page content via JavaScript and APIs (AJAX/Fetch) without reloading the entire page.
- Examples: Gmail, Netflix, Instagram, Twitter/X.

### 3. SPA vs MPA (Multi-Page Application)
| Feature | Single Page Application (SPA) | Multi-Page Application (MPA) |
| :--- | :--- | :--- |
| **Page Reloads** | No full page reload on navigation | Full page reload on every click/navigation |
| **Speed & UX** | Feels like a native desktop/mobile app (instant) | Slower perceived performance; screen flashes white |
| **Rendering** | Client-Side Rendering (JavaScript generates HTML) | Server-Side Rendering (Server generates complete HTML) |
| **Server Load** | Lower: Server only sends JSON data via APIs | Higher: Server reconstructs and sends HTML for each page |
| **Routing** | Client-side routing (e.g., React Router) | Server-side routing handled by web server (Apache, Nginx) |

---

## ✍️ Student Action Items
1. Read the concepts above.
2. Open [`notes/learning-notes.md`](./notes/learning-notes.md) and fill in your definitions and takeaways.
3. Save any helpful diagrams or reference links in the [`resources/`](./resources/) folder.
