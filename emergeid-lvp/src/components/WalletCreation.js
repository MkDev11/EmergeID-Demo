// WalletCreation.js
import React from 'react';
import {
  googleWallet,
  facebookWallet,
  twitterWallet,
} from '@zerodevapp/wagmi/rainbowkit';
import { connectorsForWallets } from '@rainbow-me/rainbowkit';
import { SocialWalletConnector } from '@zerodevapp/wagmi';
import { ConnectButton, RainbowKitProvider } from '@rainbow-me/rainbowkit';


 function WalletCreation({ onNext }) {
  const handleCreateWallet = () => {
//({ onWalletCreated }) { 
  const defaultProjectId = '77f0cb8d-2129-43cd-9d22-d278047e8151'; // Replace with your actual project ID

  const connectors = connectorsForWallets([
    {
      groupName: 'Social',
      wallets: [
        googleWallet({ options: { projectId: defaultProjectId } }),
        facebookWallet({ options: { projectId: defaultProjectId } }),
        twitterWallet({ options: { projectId: defaultProjectId } }),
      ],
    },
  ]);
  onNext();
};
  return (
    <div>
      <h2>Create Wallet</h2>
      <SocialWalletConnector client={{ autoConnect: false, connectors }}>
        <RainbowKitProvider modalSize={'compact'}>
          <ConnectButton onConnect={handleCreateWallet} />
        </RainbowKitProvider>
      </SocialWalletConnector>
    </div>
  );
}

export default WalletCreation;
