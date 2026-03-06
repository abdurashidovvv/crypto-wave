class Base64Service:
    """Base64 kodlash va dekodlash."""

    CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    def encode(self, text: str) -> str:
        data   = text.encode("utf-8")
        result = ""

        for i in range(0, len(data), 3):
            chunk = data[i:i+3]
            if len(chunk) == 3:
                n = (chunk[0] << 16) | (chunk[1] << 8) | chunk[2]
                result += self._encode_4(n, 0)
            elif len(chunk) == 2:
                n = (chunk[0] << 16) | (chunk[1] << 8)
                result += self._encode_4(n, 1)
            elif len(chunk) == 1:
                n = chunk[0] << 16
                result += self._encode_4(n, 2)

        return result

    def decode(self, text: str) -> str:
        text         = text.replace("=", "")
        result_bytes = []

        for i in range(0, len(text), 4):
            nums = [self.CHARS.index(c) for c in text[i:i+4]]
            result_bytes.extend(self._decode_chunk(nums))

        return bytes(result_bytes).decode("utf-8")

    def _encode_4(self, n: int, padding: int) -> str:
        """24 bitli sondan 4 ta Base64 belgisi yaratadi."""
        chars  = [self.CHARS[(n >> s) & 63] for s in (18, 12, 6, 0)]
        chars[-padding:] = ["="] * padding
        return "".join(chars)

    def _decode_chunk(self, nums: list) -> list:
        """4 ta Base64 raqamdan baytlar ajratib oladi."""
        if len(nums) == 4:
            n = (nums[0] << 18) | (nums[1] << 12) | (nums[2] << 6) | nums[3]
            return [(n >> 16) & 255, (n >> 8) & 255, n & 255]
        elif len(nums) == 3:
            n = (nums[0] << 18) | (nums[1] << 12) | (nums[2] << 6)
            return [(n >> 16) & 255, (n >> 8) & 255]
        elif len(nums) == 2:
            n = (nums[0] << 18) | (nums[1] << 12)
            return [(n >> 16) & 255]
        return []