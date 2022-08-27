import React from 'react';
import ReactDOM from 'react-dom/client';

import App from './App';

import UploadImgForm from './components/UploadImgForm';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    
    <UploadImgForm /> 
  </React.StrictMode>
);
