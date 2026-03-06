import { useState } from "react";
import {
  caesarEncode, caesarDecode,
  base64Encode, base64Decode,
  aesEncode,    aesDecode,
  rsaEncode,    rsaDecode,
  rsaGenerate,
} from "../api/crypto";
import { ALGORITHMS } from "../constants/algorithms";

// Har bir algoritm uchun encode/decode funksiyalari
const ACTION_MAP = {
  caesar: { encode: caesarEncode, decode: caesarDecode },
  base64: { encode: base64Encode, decode: base64Decode },
  aes:    { encode: aesEncode,    decode: aesDecode    },
};

export function useCrypto() {
  const [algorithm,  setAlgorithm]  = useState("caesar");
  const [inputText,  setInputText]  = useState("");
  const [key,        setKey]        = useState("");
  const [result,     setResult]     = useState("");
  const [error,      setError]      = useState("");
  const [loading,    setLoading]    = useState(false);
  const [copied,     setCopied]     = useState(false);
  const [rsaPublic,  setRsaPublic]  = useState("");
  const [rsaPrivate, setRsaPrivate] = useState("");
  const [rsaLoading, setRsaLoading] = useState(false);

  const current = ALGORITHMS.find((a) => a.id === algorithm);

  const changeAlgorithm = (id) => {
    setAlgorithm(id);
    setKey("");
    setResult("");
    setError("");
  };

  const reset = () => {
    setInputText("");
    setResult("");
    setError("");
    setKey("");
  };

  const handleAction = async (action) => {
    if (!inputText.trim()) return setError("Matn kiriting!");

    setLoading(true);
    setError("");
    setResult("");

    try {
      let data;

      // RSA alohida — chunki encode/decode uchun har xil kalit
      if (algorithm === "rsa") {
        const rsaKey = action === "encode" ? rsaPublic : rsaPrivate;
        data = action === "encode"
          ? await rsaEncode(inputText, rsaKey)
          : await rsaDecode(inputText, rsaKey);
      } else {
        // Boshqa algoritmlar ACTION_MAP orqali
        const fn = ACTION_MAP[algorithm][action];
        data = await fn(inputText, key);
      }

      setResult(data.result);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const generateRSA = async () => {
    setRsaLoading(true);
    setError("");
    try {
      const data = await rsaGenerate();
      setRsaPublic(data.public_key);
      setRsaPrivate(data.private_key);
    } catch (err) {
      setError(err.message);
    } finally {
      setRsaLoading(false);
    }
  };

  const copyResult = () => {
    navigator.clipboard.writeText(result);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const useAsInput = () => {
    setInputText(result);
    setResult("");
    setError("");
  };

  return {
    // State
    algorithm, inputText, key, result,
    error, loading, copied,
    rsaPublic, rsaPrivate, rsaLoading,
    current,

    // Setters
    setInputText, setKey,
    setRsaPublic, setRsaPrivate,

    // Actions
    changeAlgorithm,
    handleAction,
    generateRSA,
    copyResult,
    useAsInput,
    reset,
  };
}