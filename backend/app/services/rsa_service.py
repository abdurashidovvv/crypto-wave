from app.utils.math_utils import (
    generate_prime, mod_pow,
    mod_inverse, int_to_bytes, bytes_to_int
)

class RsaService:
    """RSA-512 asimmetrik shifrlash."""

    RSA_E = 65537  # Standart ochiq ko'rsatkich

    def generate_keys(self) -> dict:
        p, q = self._generate_distinct_primes(256)
        n    = p * q
        phi  = (p - 1) * (q - 1)
        d    = mod_inverse(self.RSA_E, phi)
        return {
            "public_key":  f"{hex(self.RSA_E)}:{hex(n)}",
            "private_key": f"{hex(d)}:{hex(n)}",
            "n_bits":      n.bit_length()
        }

    def encode(self, text: str, key: str) -> str:
        if not key:
            raise ValueError("RSA shifrlash uchun public key kerak!")
        e, n = self._parse_key(key)
        m    = bytes_to_int(text.encode("utf-8"))
        if m >= n:
            raise ValueError("Matn juda uzun! RSA-512 uchun 53 baytdan oshmasin.")
        return hex(mod_pow(m, e, n))

    def decode(self, text: str, key: str) -> str:
        if not key:
            raise ValueError("RSA deshifrlash uchun private key kerak!")
        d, n = self._parse_key(key)
        c    = int(text, 16)
        return int_to_bytes(mod_pow(c, d, n)).decode("utf-8")

    def _generate_distinct_primes(self, bits: int) -> tuple:
        """Ikki har xil tub son yaratadi."""
        p = generate_prime(bits)
        q = generate_prime(bits)
        while p == q:
            q = generate_prime(bits)
        return p, q

    def _parse_key(self, key: str) -> tuple:
        """'hex_a:hex_b' formatdagi kalitni (a, b) ga aylantiradi."""
        try:
            a_hex, b_hex = key.split(":")
            return int(a_hex, 16), int(b_hex, 16)
        except Exception:
            raise ValueError("Noto'g'ri kalit formati! Kutilgan: hex:hex")