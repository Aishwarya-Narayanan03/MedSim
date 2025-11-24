import React, { useState } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

export const SemanticSearch: React.FC = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<any[]>([]);
  const handleSearch = async () => {
    // TODO: Call backend semantic search
    setResults([{ id: 1, text: 'Sample result for: ' + query }]);
  };
  return (
    <Box mb={3}>
      <Typography variant="h6">Semantic Search</Typography>
      <Box display="flex" gap={2} mt={1}>
        <TextField label="Search cases" value={query} onChange={e => setQuery(e.target.value)} fullWidth />
        <Button variant="contained" onClick={handleSearch}>Search</Button>
      </Box>
      <Box mt={2}>
        {results.map(r => (
          <Box key={r.id} p={2} bgcolor="grey.100" borderRadius={1} mb={1}>{r.text}</Box>
        ))}
      </Box>
    </Box>
  );
};
