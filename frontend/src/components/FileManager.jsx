import React, { useState, useEffect } from 'react';
import axios from 'axios';
import PdfViewer from './PdfViewer';

function FileManager({ onFileClick }) {
  const [systemFiles, setSystemFiles] = useState([]);
  const [customFiles, setCustomFiles] = useState([]);
  const [newFolderName, setNewFolderName] = useState('');
  const [fileToUpload, setFileToUpload] = useState(null);
  const [selectedFile, setSelectedFile] = useState(null);

  useEffect(() => {
    fetchFiles();
  }, []);

  const fetchFiles = async () => {
    const token = localStorage.getItem('token');
    const headers = { Authorization: `Bearer ${token}` };

    const systemFilesResponse = await axios.get('/api/system-files', { headers });
    setSystemFiles(systemFilesResponse.data);

    const customFilesResponse = await axios.get('/api/custom-files', { headers });
    setCustomFiles(customFilesResponse.data);
  };

  const handleCreateFolder = async (e) => {
    e.preventDefault();
    const token = localStorage.getItem('token');
    const headers = { Authorization: `Bearer ${token}` };

    await axios.post('/api/custom-files', { name: newFolderName, is_folder: true }, { headers });
    setNewFolderName('');
    fetchFiles();
  };

  const handleFileChange = (e) => {
    setFileToUpload(e.target.files[0]);
  };

  const handleFileUpload = async (e) => {
    e.preventDefault();
    const token = localStorage.getItem('token');
    const headers = { Authorization: `Bearer ${token}` };

    const formData = new FormData();
    formData.append('file', fileToUpload);

    await axios.post('/api/upload', formData, { headers });
    fetchFiles();
  };

  const handleFileClick = (file) => {
    setSelectedFile(`/api/uploads/${file.path}`);
    onFileClick(file);
  };

  return (
    <div>
      {selectedFile ? (
        <PdfViewer file={selectedFile} />
      ) : (
        <div>
          <h2>System Files</h2>
          <ul>
            {systemFiles.map(file => (
              <li key={file.id} onClick={() => handleFileClick(file)}>{file.name}</li>
            ))}
          </ul>

          <h2>Custom Files</h2>
          <form onSubmit={handleCreateFolder}>
            <input
              type="text"
              placeholder="Folder Name"
              value={newFolderName}
              onChange={(e) => setNewFolderName(e.target.value)}
            />
            <button type="submit">Create Folder</button>
          </form>

          <form onSubmit={handleFileUpload}>
            <input type="file" onChange={handleFileChange} />
            <button type="submit">Upload File</button>
          </form>

          <ul>
            {customFiles.map(file => (
              <li key={file.id} onClick={() => handleFileClick(file)}>{file.name}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default FileManager;
