from app.utils.text_utils import is_readable, load_words

UZBEK_WORDS = load_words()

class CaesarService:
    """Caesar Cipher shifrlash va deshifrlash."""

    def encode(self, text: str, key: str) -> str:
        if not key:
            raise ValueError("Caesar shifrlash uchun kalit kerak!")
        return self._shift(text, int(key) % 26)

    def decode(self, text: str, key: str) -> str:
        if key:
            return self._shift(text, -(int(key) % 26))
        return self._brute_force(text)

    def _shift(self, text: str, shift: int) -> str:
        """Matnni shift miqdorida siljitadi."""
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        return result

    def _brute_force(self, text: str) -> str:
        """Kalitsiz — barcha 26 variantni sinab o'zbek so'zlari bilan tekshiradi."""
        for shift in range(26):
            candidate = self._shift(text, -shift)
            if is_readable(candidate, UZBEK_WORDS):
                return candidate
        raise ValueError(
            "Matn avtomatik aniqlanmadi. Iltimos, kalitni qo'lda kiriting."
        )