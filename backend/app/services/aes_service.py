from app.services.base64_service import Base64Service

# --- AES konstantalar ---
SBOX = [
    0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76,
    0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0,
    0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15,
    0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75,
    0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84,
    0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf,
    0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8,
    0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2,
    0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73,
    0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb,
    0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79,
    0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08,
    0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a,
    0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e,
    0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf,
    0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16,
]
INV_SBOX = [0] * 256
for _i, _v in enumerate(SBOX):
    INV_SBOX[_v] = _i

RCON = [0x00,0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1b,0x36]


class AesService:
    """AES-128 ECB shifrlash va deshifrlash."""

    def __init__(self):
        self._b64 = Base64Service()

    def encode(self, text: str, key: str) -> str:
        if not key:
            raise ValueError("AES shifrlash uchun kalit kerak!")

        key_bytes  = self._prepare_key(key)
        data       = self._pad(text.encode("utf-8"))
        round_keys = self._key_expansion(key_bytes)

        encrypted = []
        for i in range(0, len(data), 16):
            block = list(data[i:i+16])
            encrypted.extend(self._encrypt_block(block, round_keys))

        return self._b64.encode(bytes(encrypted).decode("latin-1"))

    def decode(self, text: str, key: str) -> str:
        if not key:
            raise ValueError("AES deshifrlash uchun kalit kerak!")

        key_bytes  = self._prepare_key(key)
        data       = self._b64.decode(text).encode("latin-1")
        round_keys = self._key_expansion(key_bytes)

        decrypted = []
        for i in range(0, len(data), 16):
            block = list(data[i:i+16])
            decrypted.extend(self._decrypt_block(block, round_keys))

        return self._unpad(decrypted)

    # --- Yordamchi metodlar ---

    def _prepare_key(self, key: str) -> bytes:
        """Kalitni 16 baytga keltiradi."""
        k = key.encode("utf-8")
        return (k * ((16 // len(k)) + 1))[:16]

    def _pad(self, data: bytes) -> bytes:
        """PKCS7 padding qo'shadi."""
        pad_len = 16 - (len(data) % 16)
        return data + bytes([pad_len] * pad_len)

    def _unpad(self, data: list) -> str:
        """PKCS7 padding olib tashlaydi."""
        pad_len = data[-1]
        return bytes(data[:-pad_len]).decode("utf-8")

    def _xtime(self, a: int) -> int:
        return ((a << 1) ^ 0x1b) & 0xff if a & 0x80 else (a << 1) & 0xff

    def _gmul(self, a: int, b: int) -> int:
        result = 0
        for _ in range(8):
            if b & 1: result ^= a
            a = self._xtime(a)
            b >>= 1
        return result

    def _key_expansion(self, key: bytes) -> list:
        w = [list(key[i:i+4]) for i in range(0, 16, 4)]
        for i in range(4, 44):
            temp = w[i-1][:]
            if i % 4 == 0:
                temp = temp[1:] + temp[:1]
                temp = [SBOX[b] for b in temp]
                temp[0] ^= RCON[i // 4]
            w.append([w[i-4][j] ^ temp[j] for j in range(4)])
        return [sum([w[i+j] for j in range(4)], []) for i in range(0, 44, 4)]

    def _add_round_key(self, state: list, rk: list) -> list:
        return [state[i] ^ rk[i] for i in range(16)]

    def _sub_bytes(self, state: list) -> list:
        return [SBOX[b] for b in state]

    def _inv_sub_bytes(self, state: list) -> list:
        return [INV_SBOX[b] for b in state]

    def _shift_rows(self, s: list) -> list:
        r = s[:]
        r[1],r[5],r[9],r[13]   = s[5],s[9],s[13],s[1]
        r[2],r[6],r[10],r[14]  = s[10],s[14],s[2],s[6]
        r[3],r[7],r[11],r[15]  = s[15],s[3],s[7],s[11]
        return r

    def _inv_shift_rows(self, s: list) -> list:
        r = s[:]
        r[1],r[5],r[9],r[13]   = s[13],s[1],s[5],s[9]
        r[2],r[6],r[10],r[14]  = s[10],s[14],s[2],s[6]
        r[3],r[7],r[11],r[15]  = s[7],s[11],s[15],s[3]
        return r

    def _mix_columns(self, s: list) -> list:
        r = s[:]
        for c in range(4):
            i = c * 4
            a = s[i:i+4]
            r[i]   = self._gmul(a[0],2)^self._gmul(a[1],3)^a[2]^a[3]
            r[i+1] = a[0]^self._gmul(a[1],2)^self._gmul(a[2],3)^a[3]
            r[i+2] = a[0]^a[1]^self._gmul(a[2],2)^self._gmul(a[3],3)
            r[i+3] = self._gmul(a[0],3)^a[1]^a[2]^self._gmul(a[3],2)
        return r

    def _inv_mix_columns(self, s: list) -> list:
        r = s[:]
        for c in range(4):
            i = c * 4
            a = s[i:i+4]
            r[i]   = self._gmul(a[0],14)^self._gmul(a[1],11)^self._gmul(a[2],13)^self._gmul(a[3],9)
            r[i+1] = self._gmul(a[0],9)^self._gmul(a[1],14)^self._gmul(a[2],11)^self._gmul(a[3],13)
            r[i+2] = self._gmul(a[0],13)^self._gmul(a[1],9)^self._gmul(a[2],14)^self._gmul(a[3],11)
            r[i+3] = self._gmul(a[0],11)^self._gmul(a[1],13)^self._gmul(a[2],9)^self._gmul(a[3],14)
        return r

    def _encrypt_block(self, block: list, rks: list) -> list:
        state = self._add_round_key(block, rks[0])
        for rnd in range(1, 10):
            state = self._sub_bytes(state)
            state = self._shift_rows(state)
            state = self._mix_columns(state)
            state = self._add_round_key(state, rks[rnd])
        state = self._sub_bytes(state)
        state = self._shift_rows(state)
        return self._add_round_key(state, rks[10])

    def _decrypt_block(self, block: list, rks: list) -> list:
        state = self._add_round_key(block, rks[10])
        for rnd in range(9, 0, -1):
            state = self._inv_shift_rows(state)
            state = self._inv_sub_bytes(state)
            state = self._add_round_key(state, rks[rnd])
            state = self._inv_mix_columns(state)
        state = self._inv_shift_rows(state)
        state = self._inv_sub_bytes(state)
        return self._add_round_key(state, rks[0])