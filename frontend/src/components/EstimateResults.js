import React from 'react';

export default function EstimateResults({ results }) {
  return (
    <div>
      <h2>Estimate Analysis</h2>
      <pre>{JSON.stringify(results, null, 2)}</pre>
    </div>
  );
}
