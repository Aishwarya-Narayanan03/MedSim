import React from 'react';
import { GoogleLogin } from '@react-oauth/google';
import Box from '@mui/material/Box';
import { useNavigate } from 'react-router-dom';

export const GoogleLoginButton: React.FC = () => {
  const navigate = useNavigate();
  return (
    <Box>
      <GoogleLogin
        onSuccess={credentialResponse => {
          // Send credentialResponse.credential to your backend for verification
          console.log(credentialResponse);
          // Redirect to dashboard after successful login
          navigate('/dashboard');
        }}
        onError={() => {
          console.log('Login Failed');
        }}
      />
    </Box>
  );
};
