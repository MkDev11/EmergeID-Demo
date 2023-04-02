// Confirmation.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Confirmation({ userId }) {
  const [userDetails, setUserDetails] = useState({});

  useEffect(() => {
    const fetchUserDetails = async () => {
      const response = await axios.get(`http://localhost:5000/user/${userId}`);
      setUserDetails(response.data);
    };

    fetchUserDetails();
  }, [userId]);

  const { image, clientSideDID, tokenLink } = userDetails;

  return (
    <div>
      <h2>Confirmation</h2>
      {image && <img src={image} alt="User selfie" />}
      <p>Client-side DID: {clientSideDID}</p>
      <p>
        Token Link:{' '}
        {tokenLink && (
          <a href={tokenLink} target="_blank" rel="noopener noreferrer">
            View on PolyScan
          </a>
        )}
      </p>
    </div>
  );
}
export default Confirmation;
