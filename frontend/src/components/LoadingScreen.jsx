import { useEffect, useState } from "react";

export default function LoadingScreen({ onDone }) {
  const [progress, setProgress] = useState(0);
  const [phase, setPhase]       = useState(0);

  const phases = [
    "Algoritmlar yuklanmoqda...",
    "AES kalitlar tayyorlanmoqda...",
    "RSA parametrlar sozlanmoqda...",
    "Tayyor!",
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      setProgress((p) => {
        if (p >= 100) {
          clearInterval(interval);
          setTimeout(onDone, 400);
          return 100;
        }
        return p + 2;
      });
    }, 30);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    if (progress < 30)       setPhase(0);
    else if (progress < 60)  setPhase(1);
    else if (progress < 90)  setPhase(2);
    else                     setPhase(3);
  }, [progress]);

  return (
    <div className="loading-screen">
      <div className="loading-content">
        <div className="loading-logo">
          <span className="loading-icon">⚡</span>
          <span className="loading-title">CryptoWave</span>
        </div>
        <div className="loading-bar-wrap">
          <div className="loading-bar" style={{ width: `${progress}%` }} />
        </div>
        <p className="loading-phase">{phases[phase]}</p>
        <span className="loading-percent">{progress}%</span>
      </div>
    </div>
  );
}