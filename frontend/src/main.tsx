import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.tsx';
import './index.css';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    // Add more routes as needed
  },
  // ... other routes
]);

// Get the root element
const root = ReactDOM.createRoot(document.getElementById('root')!);

// Render the RouterProvider with the created router
root.render(<RouterProvider router={router} />);
