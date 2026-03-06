from pydantic import BaseModel

class EncryptRequest(BaseModel):
    text: str
    key: str = ""

class DecryptRequest(BaseModel):
    text: str
    key: str = ""

class CryptoResponse(BaseModel):
    result: str       # har doim str — Union kerak emas
    algorithm: str
    success: bool
    
class RSAKeysResponse(BaseModel):
    public_key: str
    private_key: str
    n_bits: int
    success: bool