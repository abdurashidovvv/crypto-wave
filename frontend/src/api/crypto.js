const BASE_URL = "https://crypto-wave-8j9w.onrender.com/api/crypto";
console.log("API URL:", import.meta.env.VITE_API_URL);
// Umumiy so'rov yuboruvchi funksiya
async function request(endpoint, body) {
  const response = await fetch(`${BASE_URL}/${endpoint}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });

  const data = await response.json();

  // Backend xato qaytarsa
  if (!response.ok) {
    throw new Error(data.detail || "Xatolik yuz berdi");
  }

  return data;
}

// --- Caesar ---
export const caesarEncode = (text, key) =>
  request("caesar/encode", { text, key });

export const caesarDecode = (text, key) =>
  request("caesar/decode", { text, key });

// --- Base64 ---
export const base64Encode = (text) =>
  request("base64/encode", { text });

export const base64Decode = (text) =>
  request("base64/decode", { text });

// --- AES ---
export const aesEncode = (text, key) =>
  request("aes/encode", { text, key });

export const aesDecode = (text, key) =>
  request("aes/decode", { text, key });

// RSA
export const rsaGenerate = () =>
  fetch("/api/crypto/rsa/generate").then(r => r.json());

export const rsaEncode = (text, key) =>
  request("rsa/encode", { text, key });

export const rsaDecode = (text, key) =>
  request("rsa/decode", { text, key });