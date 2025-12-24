import React, { useState } from 'react';
import ImageUpload from './components/ImageUpload';
import ResultDisplay from './components/ResultDisplay';
import './App.css';
import logo from './logo.png';

const App = () => {
  const [selectedOption, setSelectedOption] = useState(null);
  const [result, setResult] = useState(null);

  const handleOptionClick = (option) => {
    setSelectedOption(option);
    setResult(null); // Reset the result when switching options
  };

  const handleResult = (resultData) => {
    setResult(resultData);
  };

  return (
    <div className="app">
      <header className="header">
        <img src={logo} alt="Smart Vision Logo" className="logo" />
      </header>
      <h1>Quality Test Platform</h1>

      {!selectedOption && (
        <div className="options">
          <button onClick={() => handleOptionClick('OCR')}>Product Description</button>
          <button onClick={() => handleOptionClick('Freshness')}>Freshness Report</button>
          <button onClick={() => handleOptionClick('Quantity')}>Quantity Report</button>
        </div>
      )}

      {selectedOption && (
        <>
          <ImageUpload selectedOption={selectedOption} onResult={handleResult} />
          {result && <ResultDisplay result={result} />}
          <button className="back-button" onClick={() => setSelectedOption(null)}>
            Back to Options
          </button>
        </>
      )}
    </div>
  );
};

export default App;