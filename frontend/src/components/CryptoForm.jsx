import { useCrypto }      from "../hooks/useCrypto";
import AlgorithmTabs      from "./AlgorithmTabs";
import RsaPanel           from "./RsaPanel";
import ResultPanel        from "./ResultPanel";

export default function CryptoForm() {
  const {
    algorithm, inputText, key, result,
    error, loading, copied,
    rsaPublic, rsaPrivate, rsaLoading,
    current,
    setInputText, setKey,
    setRsaPublic, setRsaPrivate,
    changeAlgorithm,
    handleAction,
    generateRSA,
    copyResult,
    useAsInput,
    reset,
  } = useCrypto();

  return (
    <div className="crypto-form">

      {/* Algoritm tanlash */}
      <AlgorithmTabs active={algorithm} onChange={changeAlgorithm} />

      {/* RSA kalit paneli */}
      {current.isRSA && (
        <RsaPanel
          publicKey={rsaPublic}
          privateKey={rsaPrivate}
          onPublicChange={setRsaPublic}
          onPrivateChange={setRsaPrivate}
          onGenerate={generateRSA}
          loading={rsaLoading}
        />
      )}

      {/* Matn kiritish */}
      <div className="field">
        <div className="field-label">
          <span>Matn</span>
          <span className="char-count">{inputText.length} belgi</span>
        </div>
        <textarea
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          placeholder="Shifrlash yoki deshifrlash uchun matn..."
          rows={5}
        />
      </div>

      {/* Kalit */}
      {current.needsKey && (
        <div className="field">
          <div className="field-label">
            <span>Kalit</span>
          </div>
          <input
            type="text"
            value={key}
            onChange={(e) => setKey(e.target.value)}
            placeholder={current.keyPlaceholder}
          />
        </div>
      )}

      {/* Tugmalar */}
      <div className="actions">
        <button
          className="btn btn-encode"
          onClick={() => handleAction("encode")}
          disabled={loading}
        >
          {loading ? <><div className="spinner" /> Jarayonda...</> : <>🔒 Shifrlash</>}
        </button>
        <button
          className="btn btn-decode"
          onClick={() => handleAction("decode")}
          disabled={loading}
        >
          {loading ? <><div className="spinner" /> Jarayonda...</> : <>🔓 Deshifrlash</>}
        </button>
        <button className="btn btn-clear" onClick={reset}>🗑️</button>
      </div>

      {/* Xato */}
      {error && <div className="error">⚠️ {error}</div>}

      {/* Natija */}
      {result && (
        <ResultPanel
          result={result}
          algorithm={current.label}
          copied={copied}
          onCopy={copyResult}
          onUseAsInput={useAsInput}
        />
      )}

    </div>
  );
}
