import { useState } from 'react';

// Exercise: Add a "Decrement" button that decreases count by 1
export default function CounterExercise() {
  const [count, setCount] = useState(0);

  return (
    <div style={{ fontFamily: 'sans-serif', padding: '20px' }}>
      <h3>Counter Exercise</h3>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment (+1)</button>
      {/* TODO: Add a button below to decrement count by 1 */}
    </div>
  );
}
