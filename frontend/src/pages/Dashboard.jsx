import React, { useState, useEffect } from 'react';
import FileManager from '../components/FileManager';
import RecentActivityBar from '../components/RecentActivityBar';
import Profile from '../components/Profile';

function Dashboard() {
  const [recentFiles, setRecentFiles] = useState([]);

  useEffect(() => {
    const storedRecentFiles = JSON.parse(localStorage.getItem('recentFiles')) || [];
    setRecentFiles(storedRecentFiles);
  }, []);

  const handleFileClick = (file) => {
    const updatedRecentFiles = [file, ...recentFiles.filter(f => f.id !== file.id)].slice(0, 5);
    setRecentFiles(updatedRecentFiles);
    localStorage.setItem('recentFiles', JSON.stringify(updatedRecentFiles));
  };

  return (
    <div className="app-container">
      <div className="panel recent-activity-bar">
        <RecentActivityBar recentFiles={recentFiles} onFileClick={handleFileClick} />
      </div>
      <div className="panel main-application-bar">
        <FileManager onFileClick={handleFileClick} />
      </div>
      <div className="panel user-account-bar">
        <Profile />
      </div>
    </div>
  );
}

export default Dashboard;
