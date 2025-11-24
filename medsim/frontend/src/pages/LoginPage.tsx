import React from 'react';
import { GoogleLogin } from '@react-oauth/google';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

const LoginPage: React.FC = () => (
  <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center" minHeight="100vh">
    <Typography variant="h3" mb={4} fontWeight={700} color="primary">MedSim Login</Typography>
    <GoogleLogin
      onSuccess={credentialResponse => {
        // Send credentialResponse.credential to your backend for verification
        console.log(credentialResponse);
      }}
      onError={() => {
        console.log('Login Failed');
      }}
    />
  </Box>
);

export default LoginPage;