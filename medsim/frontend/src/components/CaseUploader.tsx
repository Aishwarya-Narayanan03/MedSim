import React, { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';

export const CaseUploader: React.FC = () => {
  const onDrop = useCallback((acceptedFiles: File[]) => {
    // TODO: Upload to backend
    alert(`Uploading: ${acceptedFiles.map(f => f.name).join(', ')}`);
  }, []);
  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop, accept: { 'application/pdf': [], 'image/*': [], 'application/msword': [], 'application/vnd.openxmlformats-officedocument.wordprocessingml.document': [] } });
  return (
    <Box {...getRootProps()} border={2} borderColor={isDragActive ? 'primary.main' : 'grey.400'} borderRadius={2} p={3} textAlign="center" mb={3} sx={{ cursor: 'pointer', transition: 'border-color 0.2s' }}>
      <input {...getInputProps()} />
      <CloudUploadIcon sx={{ fontSize: 48, color: 'primary.main', mb: 1 }} />
      <Typography variant="h6">Drag & drop a case file here, or click to select</Typography>
      <Button variant="outlined" sx={{ mt: 2 }}>Browse Files</Button>
    </Box>
  );
};
