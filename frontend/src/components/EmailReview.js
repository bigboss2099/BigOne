import React from 'react';

export default function EmailReview({ summary, reply }) {
  return (
    <div>
      <h2>Email Summary</h2>
      <p>{summary}</p>
      <h3>Draft Reply</h3>
      <textarea defaultValue={reply} />
    </div>
  );
}
