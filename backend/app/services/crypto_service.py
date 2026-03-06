from app.services.caesar_service import CaesarService
from app.services.base64_service  import Base64Service
from app.services.aes_service     import AesService
from app.services.rsa_service     import RsaService

class CryptoService:
    """
    Barcha shifrlash servislarini birlashtiruvchi delegat.
    O'zi hech qanday algoritm bajarmaydi —
    faqat tegishli servislarga yo'naltiradi.
    """

    def __init__(self):
        self._caesar = CaesarService()
        self._base64 = Base64Service()
        self._aes    = AesService()
        self._rsa    = RsaService()

    # --- Caesar ---
    def caesar_encode(self, text: str, key: str) -> str:
        return self._caesar.encode(text, key)

    def caesar_decode(self, text: str, key: str) -> str:
        return self._caesar.decode(text, key)

    # --- Base64 ---
    def base64_encode(self, text: str) -> str:
        return self._base64.encode(text)

    def base64_decode(self, text: str) -> str:
        return self._base64.decode(text)

    # --- AES ---
    def aes_encode(self, text: str, key: str) -> str:
        return self._aes.encode(text, key)

    def aes_decode(self, text: str, key: str) -> str:
        return self._aes.decode(text, key)

    # --- RSA ---
    def rsa_generate_keys(self) -> dict:
        return self._rsa.generate_keys()

    def rsa_encode(self, text: str, key: str) -> str:
        return self._rsa.encode(text, key)

    def rsa_decode(self, text: str, key: str) -> str:
        return self._rsa.decode(text, key)
