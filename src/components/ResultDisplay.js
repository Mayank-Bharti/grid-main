// components/ResultDisplay.js
import React from 'react';

const ResultDisplay = ({ result }) => {
  if (Array.isArray(result)) {
    return (
      <div className="result-display">
        <h2>Result</h2>
        <table className="result-table">
          <thead>
            <tr>
              <th>Field</th>
              <th>Value</th>
            </tr>
          </thead>
          <tbody>
          {result.map((item, index) => (
            <tr key={index}>
              <td>{item.itemName || item.label}</td> 
              <td>{item.count || item.value}</td> {/* Use item.count if available */}
            </tr>
          ))}
        </tbody>
          {/* <tbody>
            {result.map((item, index) => (
              <tr key={index}>
                <td>{item.label}</td>
                <td>{item.value}</td>
              </tr>
            ))}
          </tbody> */}
        </table>
      </div>
    );
  } else {
    // Check if the result is "Expired"
    if (result === 'Expired') {
      return (
        <div className="result-display">
          <h2>Result</h2>
          <p>{result}</p> {/* Just display "Expired" */}
        </div>
      );
    } else {
      // Extract days from the result if it's in a specific format
      const daysMatch = result.match(/\((\d+)-(\d+)\)/);
      if (daysMatch) {
        const minDays = parseInt(daysMatch[1], 10);
        const maxDays = parseInt(daysMatch[2], 10);
        
        // Check if the minimum days are more than 15
        if (minDays>=10) {
          return (
            <div className="result-display">
              <h2>Result</h2>
              <p>{result} - About to Expire</p> {/* Append "About to Expire" */}
            </div>
          );
        } else {
          return (
            <div className="result-display">
              <h2>Result</h2>
              <p>{result} "Fresh"</p> {/* Append "days left to expire" */}
            </div>
          );
        }
      }
    }
  }
};

export default ResultDisplay;
