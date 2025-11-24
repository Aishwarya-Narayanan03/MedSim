import React, { useState } from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

export const LLMCaseEval: React.FC = () => {
  const [evaluating, setEvaluating] = useState(false);
  const [result, setResult] = useState<string | null>(null);
  const handleEval = async () => {
    setEvaluating(true);
    // TODO: Call backend LLM evaluation
    setTimeout(() => {
      setResult('LLM evaluation result: (mocked)');
      setEvaluating(false);
    }, 1200);
  };
  return (
    <Box mb={3}>
      <Typography variant="h6">Run LLM Evaluation</Typography>
      <Button variant="contained" onClick={handleEval} disabled={evaluating} sx={{ ml: 2 }}>
        {evaluating ? 'Evaluating...' : 'Run Evaluation'}
      </Button>
      {result && <Box mt={2} p={2} bgcolor="grey.100" borderRadius={1}>{result}</Box>}
    </Box>
  );
};
