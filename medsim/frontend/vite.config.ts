import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  root: '.', // project root
  publicDir: 'public', // public directory
  plugins: [react()],
  build: {
    outDir: 'dist',
  },
  server: {
    port: 4000,
    open: true,
  },
});
