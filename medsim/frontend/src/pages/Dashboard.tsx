import React from 'react';
import Container from '@mui/material/Container';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import { LLMCaseEval } from '../components/LLMCaseEval';
import { SemanticSearch } from '../components/SemanticSearch';
import { HistoryList } from '../components/HistoryList';

const Dashboard: React.FC = () => (
  <Container maxWidth="md" sx={{ mt: 4 }}>
    <Card sx={{ mb: 4, boxShadow: 3 }}>
      <CardContent>
        <Typography variant="h4" fontWeight={700} color="primary" gutterBottom>
          Welcome to MedSim Dashboard!
        </Typography>
        <Divider sx={{ mb: 2 }} />
        <LLMCaseEval />
        <Divider sx={{ my: 2 }} />
        <SemanticSearch />
        <Divider sx={{ my: 2 }} />
        <HistoryList />
      </CardContent>
    </Card>
  </Container>
);

export default Dashboard;