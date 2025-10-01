import React from 'react';

function RecentActivityBar({ recentFiles, onFileClick }) {
  return (
    <div>
      <h2>Recent Activity</h2>
      <ul>
        {recentFiles.map(file => (
          <li key={file.id} onClick={() => onFileClick(file)}>{file.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default RecentActivityBar;
