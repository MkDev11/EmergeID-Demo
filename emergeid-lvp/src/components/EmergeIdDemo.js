import React, { useState } from 'react';
import WalletCreation from './WalletCreation';
import ImageUpload from './ImageUpload';
import SignInWithIdMe from './SignInWithIdMe';
import Confirmation from './Confirmation';

function EmergeIdDemo() {
  const [step, setStep] = useState(0);

  const handleNextStep = () => {
    setStep((prevStep) => prevStep + 1);
  };

  return (
    <div>
      {step === 0 && <WalletCreation onNext={handleNextStep} />}
      {step === 1 && <ImageUpload onNext={handleNextStep} />}
      {step === 2 && <SignInWithIdMe onNext={handleNextStep} />}
      {step === 3 && <Confirmation />}
    </div>
  );
}
export default EmergeIdDemo;