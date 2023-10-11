import React, { useState, useEffect } from 'react';
import './styles.css'; // Importa el archivo CSS

function App() {
  const [currentDateTime, setCurrentDateTime] = useState(new Date());

  useEffect(() => {
    const intervalId = setInterval(() => {
      setCurrentDateTime(new Date());
    }, 1000);

    return () => {
      clearInterval(intervalId);
    };
  }, []);

  return (
    <div className="App">
      <h1>Bienvenido </h1>
      <p>Fecha y hora actuales: {currentDateTime.toLocaleString()}</p>
    </div>
  );
}

export default App;
