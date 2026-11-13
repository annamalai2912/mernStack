# 📌 Module 02: React vs Traditional Web Development

## 🎯 Learning Objectives
By the end of this module, you should be able to:
1. Explain the difference between **Imperative** and **Declarative** programming.
2. Understand what the **Real DOM** is and why direct DOM manipulation is costly/slow.
3. Understand the **Virtual DOM (VDOM)**, **Reconciliation**, and the **Diffing Algorithm**.
4. Compare Vanilla JS DOM manipulation with React's component-based state updates.

---

## 📖 Key Concepts

### 1. Imperative vs Declarative
- **Traditional (Imperative):** You tell the browser **HOW** to do every single step.
  ```javascript
  // Imperative Vanilla JS
  const btn = document.createElement('button');
  btn.innerText = 'Clicks: 0';
  let count = 0;
  btn.addEventListener('click', () => {
    count++;
    btn.innerText = `Clicks: ${count}`;
  });
  document.body.appendChild(btn);
  ```
- **React (Declarative):** You declare **WHAT** the UI should look like for a given state, and React handles DOM updates.
  ```jsx
  // Declarative React
  function Counter() {
    const [count, setCount] = useState(0);
    return <button onClick={() => setCount(count + 1)}>Clicks: {count}</button>;
  }
  ```

### 2. What is the Real DOM?
- The Document Object Model (DOM) is an in-memory tree representation of HTML elements.
- **Why is Real DOM manipulation slow?**  
  Modifying the real DOM triggers browser **Reflow** (recalculating element layouts and geometry) and **Repaint** (drawing pixels on screen). Doing this repeatedly causes UI jank and performance degradation.

### 3. The Virtual DOM (VDOM)
- A lightweight JavaScript object that mirrors the structure of the Real DOM.
- Kept in memory and synchronized with the Real DOM by libraries like ReactDOM.

### 4. How Reconciliation & Diffing Work:
1. **Initial Render:** React creates a Virtual DOM tree of the UI.
2. **State / Props Change:** React produces a new Virtual DOM tree.
3. **Diffing Algorithm:** React compares the new VDOM with the previous VDOM (`O(n)` heuristic algorithm).
4. **Reconciliation & Batch Update:** React calculates the minimum number of changes needed and efficiently updates ONLY those specific nodes in the Real DOM.

---

## ✍️ Student Action Items
1. Review the comparison example in [`comparison-code/vanilla-vs-react.md`](./comparison-code/vanilla-vs-react.md).
2. Open [`notes/learning-notes.md`](./notes/learning-notes.md) and fill in your notes.
3. Practice explaining the Virtual DOM in 60 seconds as if you were in an interview.
