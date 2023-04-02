// UploadSelfie.js
import React, { useState } from 'react';
import axios from 'axios';

function ImageUpload({ onImageUploaded }) {
  const [selectedFile, setSelectedFile] = useState(null);

  const onFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const onFileUpload = async () => {
    const formData = new FormData();
    formData.append('image', selectedFile);
    const response = await axios.post('http://localhost:5000/upload', formData);
    onImageUploaded(response.data);
  };

  return (
    <div>
      <h2>Upload Selfie</h2>
      <input type="file" onChange={onFileChange} />
      <button onClick={onFileUpload}>Upload</button>
    </div>
  );
}
export default ImageUpload;