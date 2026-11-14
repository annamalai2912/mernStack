import { useState } from 'react';

// Placement Technical Interview Task: State Counter
export default function InterviewCounter() {
  const [count, setCount] = useState(0);

  return (
    <div style={{ fontFamily: 'sans-serif', padding: '20px' }}>
      <h3>Interview Task: Counter Component</h3>
      <p>Current Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>+ Increment</button>
      <button onClick={() => setCount(count - 1)} style={{ margin: '0 8px' }}>- Decrement</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}
