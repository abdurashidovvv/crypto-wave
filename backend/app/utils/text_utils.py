import re
import os

# O'zbek tilida apostrof variantlari
APOSTROPHS = [
    "\u0060",  # ` backtick
    "\u02BB",  # ʻ modifier letter
    "\u2018",  # ' left quote
    "\u2019",  # ' right quote
]

def normalize(text: str) -> str:
    """Barcha apostrof variantlarini oddiy apostrofga kamaytiradi."""
    for apos in APOSTROPHS:
        text = text.replace(apos, "'")
    return text

def load_words() -> set:
    """words.txt faylidan o'zbek so'zlarini yuklaydi."""
    words_path = os.path.join(os.path.dirname(__file__), "..", "words.txt")
    try:
        with open(words_path, "r", encoding="utf-8") as f:
            return set(word.strip().lower() for word in f)
    except FileNotFoundError:
        return set()

def is_readable(text: str, uzbek_words: set) -> bool:
    """Matn o'zbek tilida ma'nolimi yoki yo'qmi."""
    text = normalize(text.lower())
    words = re.findall(r"[a-z']+", text)
    words = [w.strip("'") for w in words if len(w.strip("'")) >= 3]

    if len(words) < 2:
        return False

    matched = sum(1 for w in words if w in uzbek_words)
    return matched / len(words) >= 0.4