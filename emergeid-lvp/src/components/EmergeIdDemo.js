import React, { useState } from 'react';
import WalletCreation from './WalletCreation';
import ImageUpload from './ImageUpload';
import SignInWithIdMe from "./SignInWithIdMe";
import Confirmation from "./Confirmation";

function EmergeIdDemo() {
  const [step, setStep] = useState(0);

  const onNext = () => {
    setStep((prevStep) => prevStep + 1);
  };

 return (
    <div>
      {step === 0 && <WalletCreation onNext={onNext} />}
      {step === 1 && <ImageUpload onNext={onNext} />}
      {step === 2 && <SignInWithIdMe onNext={onNext} />}
      {step === 3 && <Confirmation />}
    </div>
  );
}

export default EmergeIdDemo;