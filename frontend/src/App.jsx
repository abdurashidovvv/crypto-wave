import { useState } from "react";
import { useTheme } from "./ThemeContext";
import CryptoForm from "./components/CryptoForm";
import LoadingScreen from "./components/LoadingScreen";

export default function App() {
  const [loaded, setLoaded] = useState(false);
  const { theme, toggle }   = useTheme();

  if (!loaded) {
    return <LoadingScreen onDone={() => setLoaded(true)} />;
  }

  return (
    <div className="app">
      <header>
        <div className="header-top">
          <div className="header-badge">⚡ Encryption Tool</div>
          <button className="theme-toggle" onClick={toggle}>
            {theme === "dark" ? "☀️ Yorug'" : "🌙 Qorong'i"}
          </button>
        </div>
        <h1><span className="gradient-text">CryptoWave</span></h1>
        <p>Matnlarni xavfsiz shifrlang va deshifrlang</p>
      </header>

      <main>
        <CryptoForm />
      </main>

      <div className="info-grid">
        <div className="info-card">
          <div className="info-icon">🏛️</div>
          <h3>Caesar Cipher</h3>
          <p>Harflarni alfavitda siljitish. Brute force bilan kalitni avtomatik topadi.</p>
        </div>
        <div className="info-card">
          <div className="info-icon">🔤</div>
          <h3>Base64</h3>
          <p>Binary ma'lumotni matn ko'rinishiga o'tkazish. API va emailda keng ishlatiladi.</p>
        </div>
        <div className="info-card">
          <div className="info-icon">🔐</div>
          <h3>AES-128 ECB</h3>
          <p>Simmetrik shifrlash. Har 16 baytlik blok alohida kalit bilan shifrlangan.</p>
        </div>
        <div className="info-card">
          <div className="info-icon">🗝️</div>
          <h3>RSA-512</h3>
          <p>Asimmetrik shifrlash. Public key bilan shifrlash, private key bilan deshifrlash.</p>
        </div>
      </div>

      <footer>
        CRYPTOWAVE • CAESAR • BASE64 • AES-128 • RSA-512
      </footer>
    </div>
  );
}