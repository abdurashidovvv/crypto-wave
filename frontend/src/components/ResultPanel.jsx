export default function ResultPanel({ result, algorithm, copied, onCopy, onUseAsInput }) {
  return (
    <div className="result">
      <div className="result-header">
        <div className="result-label">
          <span>Natija</span>
          <span className="result-badge">{algorithm}</span>
        </div>
      </div>

      <textarea value={result} readOnly rows={5} />

      <div className="result-actions">
        <button className="btn-copy" onClick={onCopy}>
          {copied ? "✅ Nusxalandi!" : "📋 Nusxalash"}
        </button>
        <button className="btn-use" onClick={onUseAsInput}>
          ⬆️ Inputga ko'chirish
        </button>
      </div>
    </div>
  );
}