# ⚡ 2-Minute Quick Revision: React Fundamentals & JSX

| Concept | Golden Rule / Key Formula | Common Interview Pitfall |
| :--- | :--- | :--- |
| **React Definition** | Library for building User Interfaces (View layer only) | Calling React a "framework" |
| **UI Paradigm** | $UI = f(State)$ (Declarative) | Thinking you need `document.getElementById` |
| **Virtual DOM** | In-memory JS object representation of the Real DOM | Saying VDOM is "faster than the browser itself" (it minimizes reflows/repaints) |
| **Diffing & Reconciliation** | $O(n)$ heuristic comparison finding minimal real DOM updates | Confusing diffing (calculation) with reconciliation (updating DOM) |
| **SPA** | 1 HTML file + client-side routing + JSON APIs | Forgetting to mention why initial bundle might be larger |
| **JSX** | Syntactic sugar for `React.createElement(type, props, ...children)` | Saying browsers natively understand JSX |
| **Component Name** | Must be `PascalCase` | Writing lowercase (`<card />`) which React thinks is an HTML tag |
| **Fragments** | `<>...</>` prevents unnecessary DOM wrapper nodes | Wrapping everything in extra `<div>` elements |
| **List Keys** | Must be stable and unique across sibling elements (e.g. `item.id`) | Using array `index` as a key when list is dynamic/sortable |
| **Vite Speed** | Native ESM in browser + `esbuild` written in Go | Thinking Vite is only for Vue or that it bundles on dev start |
