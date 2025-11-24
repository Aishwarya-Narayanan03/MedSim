import React, { createContext, useContext } from 'react';

type AuthContextType = {
  user: any;
  isVerified: boolean;
  loading: boolean;
  signInWithGoogle: () => void;
};

const AuthContext = createContext<AuthContextType>({
  user: null,
  isVerified: false,
  loading: false,
  signInWithGoogle: () => {},
});

export const useAuth = () => useContext(AuthContext);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  // Dummy values for demonstration; replace with real logic
  const value: AuthContextType = {
    user: null,
    isVerified: false,
    loading: false,
    signInWithGoogle: () => {},
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};
