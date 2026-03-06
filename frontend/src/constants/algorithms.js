// Barcha algoritmlar haqida ma'lumot — bir joyda
export const ALGORITHMS = [
  {
    id:             "caesar",
    label:          "🏛️ Caesar",
    needsKey:       true,
    keyPlaceholder: "Shift raqami (masalan: 3)",
    isRSA:          false,
  },
  {
    id:             "base64",
    label:          "🔤 Base64",
    needsKey:       false,
    keyPlaceholder: "",
    isRSA:          false,
  },
  {
    id:             "aes",
    label:          "🔐 AES-128",
    needsKey:       true,
    keyPlaceholder: "Maxfiy kalit",
    isRSA:          false,
  },
  {
    id:             "rsa",
    label:          "🗝️ RSA-512",
    needsKey:       false,
    keyPlaceholder: "",
    isRSA:          true,
  },
];