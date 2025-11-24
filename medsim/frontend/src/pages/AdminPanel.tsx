import React from 'react';
import { CaseUploader } from '../components/CaseUploader';
import { AdminVerification } from '../components/AdminVerification';

const AdminPanel: React.FC = () => {
  return (
    <div>
      <h1>Admin Panel</h1>
      <CaseUploader />
      <AdminVerification />
      {/* Add admin functionality here */}
    </div>
  );
};

export default AdminPanel;
