import React from 'react';

export default function Dashboard({ stats }) {
  return (
    <div>
      <h2>Dashboard</h2>
      <pre>{JSON.stringify(stats, null, 2)}</pre>
    </div>
  );
}
