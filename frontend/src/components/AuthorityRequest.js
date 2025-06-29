import React from 'react';

export default function AuthorityRequest({ memo }) {
  return (
    <div>
      <h2>Authority Request</h2>
      <pre>{memo}</pre>
      <button>Approve</button>
    </div>
  );
}
