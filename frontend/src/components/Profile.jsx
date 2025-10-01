import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import { ColorModeContext } from '../ThemeContext';
import { Button } from '@mui/material';

function Profile() {
  const [username, setUsername] = useState('');
  const [profilePicture, setProfilePicture] = useState(null);
  const colorMode = useContext(ColorModeContext);

  useEffect(() => {
    const fetchProfile = async () => {
      const token = localStorage.getItem('token');
      const headers = { Authorization: `Bearer ${token}` };
      const response = await axios.get('/api/profile', { headers });
      setUsername(response.data.username);
      // setProfilePicture(response.data.profile_picture);
    };
    fetchProfile();
  }, []);

  const handleProfilePictureChange = (e) => {
    setProfilePicture(e.target.files[0]);
  };

  const handleProfilePictureUpload = async () => {
    const token = localStorage.getItem('token');
    const headers = { Authorization: `Bearer ${token}` };
    const formData = new FormData();
    formData.append('profile_picture', profilePicture);
    await axios.post('/api/profile/picture', formData, { headers });
    alert('Profile picture updated!');
  };

  return (
    <div>
      <h3>Welcome, {username}</h3>
      <div>
        <h4>Profile Picture</h4>
        <input type="file" onChange={handleProfilePictureChange} />
        <button onClick={handleProfilePictureUpload}>Upload</button>
      </div>
      <div>
        <h4>Change Password</h4>
        {/* Password change form will go here */}
      </div>
      <Button onClick={colorMode.toggleColorMode}>Toggle Theme</Button>
    </div>
  );
}

export default Profile;
