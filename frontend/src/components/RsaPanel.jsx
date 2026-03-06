export default function RsaPanel({
  publicKey, privateKey,
  onPublicChange, onPrivateChange,
  onGenerate, loading,
}) {
  return (
    <div className="rsa-panel">
      <div className="rsa-panel-header">
        <span className="rsa-panel-title">RSA Kalitlar</span>
        <button
          className="btn-generate"
          onClick={onGenerate}
          disabled={loading}
        >
          {loading
            ? <><div className="spinner" /> Yaratilmoqda...</>
            : <>⚡ Yangi kalit yaratish</>
          }
        </button>
      </div>

      <div className="rsa-keys">
        <div className="rsa-key-box">
          <label>Public Key (Shifrlash uchun)</label>
          <textarea
            value={publicKey}
            onChange={(e) => onPublicChange(e.target.value)}
            placeholder="Public key..."
            rows={3}
          />
        </div>
        <div className="rsa-key-box">
          <label>Private Key (Deshifrlash uchun)</label>
          <textarea
            value={privateKey}
            onChange={(e) => onPrivateChange(e.target.value)}
            placeholder="Private key..."
            rows={3}
          />
        </div>
      </div>
    </div>
  );
}