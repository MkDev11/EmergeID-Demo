# Emerge-ID LVP Demo App

Emerge-ID LVP is a demo app showcasing a simple identity verification process using ZeroDev SDK for wallet creation, social sign-on, Id.me authentication, and image upload.

## Features

- Wallet creation with ZeroDev SDK
- Social sign-on (Google, Apple, Facebook, etc.)
- Image upload for selfie submission
- Id.me authentication for identity verification
- Display confirmation page with user's image, client-side DID, and token link on Polyscan

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) >= 14.x.x
- [NPM](https://www.npmjs.com/) >= 6.x.x

### Installation

1. Clone the repository:
git clone https://github.com/MkDev11/EmergeID-demo.git

Navigate to the emergeid-lvp directory:
cd EmergeID-demo/emergeid-lvp

Install the required dependencies:
npm install

Set up the required environment variables by creating a .env file in the emergeid-lvp directory and filling it with the appropriate values:

REACT_APP_BACKEND_URL=<your_backend_url>
REACT_APP_IDME_CLIENT_ID=<your_idme_client_id>
REACT_APP_IDME_REDIRECT_URI=<your_idme_redirect_uri>

Start the development server:

npm start
The application will be accessible at http://localhost:3000.

License
This project is licensed under the MIT License. See the LICENSE file for more information.

javascript
Copy code

This README.md provides an overview of the Emerge-ID LVP demo app, its features, and instructions on how to set it up locally. Make sure to replace `<your_backend_url>`, `<your_idme_client_id>`, and `<your_idme_redirect_uri>` with the appropriate values in the `.env` file.