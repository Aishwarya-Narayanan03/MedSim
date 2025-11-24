import React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

export const HistoryList: React.FC = () => {
  // TODO: Fetch from backend
  const history = [
    { id: 1, action: 'Uploaded case.pdf', date: '2025-11-24' },
    { id: 2, action: 'Ran LLM evaluation', date: '2025-11-24' },
  ];
  return (
    <Box mb={3}>
      <Typography variant="h6">History</Typography>
      {history.map(item => (
        <Box key={item.id} p={2} bgcolor="grey.100" borderRadius={1} mb={1}>
          <Typography>{item.action}</Typography>
          <Typography variant="caption" color="text.secondary">{item.date}</Typography>
        </Box>
      ))}
    </Box>
  );
};
