import React, { useState, useEffect } from 'react';
import axios from 'axios';

function AdminDashboard() {
  const [users, setUsers] = useState([]);
  const [selectedUserFiles, setSelectedUserFiles] = useState([]);

  useEffect(() => {
    const fetchUsers = async () => {
      const token = localStorage.getItem('token');
      const headers = { Authorization: `Bearer ${token}` };
      const response = await axios.get('/api/admin/users', { headers });
      setUsers(response.data);
    };
    fetchUsers();
  }, []);

  const fetchUserFiles = async (userId) => {
    const token = localStorage.getItem('token');
    const headers = { Authorization: `Bearer ${token}` };
    const response = await axios.get(`/api/admin/users/${userId}/custom-files`, { headers });
    setSelectedUserFiles(response.data);
  };

  return (
    <div>
      <h1>Admin Dashboard</h1>
      <h2>Users</h2>
      <ul>
        {users.map(user => (
          <li key={user.id} onClick={() => fetchUserFiles(user.id)}>
            {user.username} {user.is_admin && '(Admin)'}
          </li>
        ))}
      </ul>

      {selectedUserFiles.length > 0 && (
        <div>
          <h2>Selected User Files</h2>
          <ul>
            {selectedUserFiles.map(file => (
              <li key={file.id}>{file.name}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default AdminDashboard;