import React, { useState } from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

export const AdminVerification: React.FC = () => {
  const [verified, setVerified] = useState(false);
  const handleVerify = async () => {
    // TODO: Call backend to verify user
    setVerified(true);
  };
  return (
    <Box>
      <Typography variant="body1">Click to verify user as admin.</Typography>
      <Button variant="contained" color="secondary" onClick={handleVerify} sx={{ mt: 2 }}>
        {verified ? 'Verified!' : 'Verify'}
      </Button>
    </Box>
  );
};
