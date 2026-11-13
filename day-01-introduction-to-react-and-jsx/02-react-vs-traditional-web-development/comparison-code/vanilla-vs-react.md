# 💻 Code Comparison: Vanilla JS vs React

Here is a side-by-side comparison of adding an item to a list.

---

### Approach 1: Vanilla JavaScript (Imperative)
```html
<input id="itemInput" type="text" placeholder="Enter task..." />
<button id="addBtn">Add</button>
<ul id="itemList"></ul>

<script>
  const input = document.getElementById('itemInput');
  const addBtn = document.getElementById('addBtn');
  const list = document.getElementById('itemList');

  addBtn.addEventListener('click', () => {
    const text = input.value.trim();
    if (text) {
      // Step-by-step DOM manipulation (Imperative)
      const li = document.createElement('li');
      li.textContent = text;
      list.appendChild(li);
      input.value = '';
    }
  });
</script>
```

---

### Approach 2: React (Declarative)
```jsx
import React, { useState } from 'react';

export default function TodoList() {
  const [items, setItems] = useState([]);
  const [text, setText] = useState('');

  const handleAdd = () => {
    if (text.trim()) {
      setItems([...items, text]);
      setText('');
    }
  };

  return (
    <div>
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter task..."
      />
      <button onClick={handleAdd}>Add</button>
      <ul>
        {items.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
}
```

---

### 🔍 Key Differences
1. **DOM Access:** React does not require `document.getElementById` or `document.querySelector`.
2. **State-Driven:** In React, the UI is a direct reflection of application state: $UI = f(State)$.
3. **Maintainability:** As applications grow, declarative code is easier to debug, test, and scale.
