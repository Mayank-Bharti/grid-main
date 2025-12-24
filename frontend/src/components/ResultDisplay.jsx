import React from "react";

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
                <td>{item.count || item.value}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  } else {
    // Handle non-array results
    let displayText = result;

    // Append status if result has day info
    const daysMatch = result.match(/\((\d+)-(\d+)\)/);
    if (daysMatch) {
      const minDays = parseInt(daysMatch[1], 10);
      displayText =
        minDays >= 10 ? `${result} - About to Expire` : `${result} - Fresh`;
    }

    return (
      <div className="result-display">
        <h2>Result</h2>
        <p>{displayText}</p>
      </div>
    );
  }
};

export default ResultDisplay;
