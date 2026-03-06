import random

def mod_pow(base: int, exp: int, mod: int) -> int:
    """Tez darajaga ko'tarish: base^exp mod mod."""
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result

def extended_gcd(a: int, b: int) -> tuple:
    """Kengaytirilgan Evklid algoritmi: a*x + b*y = gcd(a,b)."""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    return gcd, y1 - (b // a) * x1, x1

def mod_inverse(e: int, phi: int) -> int:
    """e ning phi bo'yicha modulli teskarisi: e*d ≡ 1 (mod phi)."""
    gcd, x, _ = extended_gcd(e % phi, phi)
    if gcd != 1:
        raise ValueError("Modulli teskari mavjud emas!")
    return x % phi

def miller_rabin(n: int, k: int = 10) -> bool:
    """Miller-Rabin probabilistik tub son testi."""
    if n < 2:   return False
    if n in (2, 3): return True
    if n % 2 == 0:  return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = mod_pow(a, d, n)

        if x in (1, n - 1):
            continue

        for _ in range(r - 1):
            x = mod_pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def generate_prime(bits: int) -> int:
    """Berilgan bitlik tub son yaratadi."""
    while True:
        n = random.getrandbits(bits)
        n |= (1 << bits - 1)
        n |= 1
        if miller_rabin(n):
            return n

def int_to_bytes(n: int) -> bytes:
    """Katta sonni bytes ga aylantiradi."""
    length = (n.bit_length() + 7) // 8
    return n.to_bytes(length, byteorder='big')

def bytes_to_int(b: bytes) -> int:
    """Bytes ni katta songa aylantiradi."""
    return int.from_bytes(b, byteorder='big')