from fastapi import APIRouter, HTTPException
from app.schemas.crypto import EncryptRequest, DecryptRequest, CryptoResponse, RSAKeysResponse
from app.services.crypto_service import CryptoService

router = APIRouter(prefix="/api/crypto", tags=["crypto"])

# Servisni bir marta yaratamiz
service = CryptoService()


# --- BASE64 ---
@router.post("/base64/encode", response_model=CryptoResponse)
def base64_encode(request: EncryptRequest):
    try:
        result = service.base64_encode(request.text)
        return CryptoResponse(result=result, algorithm="base64", success=True)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/base64/decode", response_model=CryptoResponse)
def base64_decode(request: DecryptRequest):
    try:
        result = service.base64_decode(request.text)
        return CryptoResponse(result=result, algorithm="base64", success=True)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# --- CAESAR ---
@router.post("/caesar/encode", response_model=CryptoResponse)
def caesar_encode(request: EncryptRequest):
    try:
        result = service.caesar_encode(request.text, request.key)
        return CryptoResponse(result=result, algorithm="caesar", success=True)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/caesar/decode", response_model=CryptoResponse)
def caesar_decode(request: DecryptRequest):
    try:
        result = service.caesar_decode(request.text, request.key)
        return CryptoResponse(result=result, algorithm="caesar", success=True)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# --- AES ---
@router.post("/aes/encode", response_model=CryptoResponse)
def aes_encode(request: EncryptRequest):
    try:
        result = service.aes_encode(request.text, request.key)
        return CryptoResponse(result=result, algorithm="aes", success=True)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/aes/decode", response_model=CryptoResponse)
def aes_decode(request: DecryptRequest):
    try:
        result = service.aes_decode(request.text, request.key)
        return CryptoResponse(result=result, algorithm="aes", success=True)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/rsa/generate", response_model=RSAKeysResponse)
def rsa_generate():
    try:
        keys = service.rsa_generate_keys()
        return RSAKeysResponse(
            public_key=keys["public_key"],
            private_key=keys["private_key"],
            n_bits=keys["n_bits"],
            success=True
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/rsa/encode", response_model=CryptoResponse)
def rsa_encode(request: EncryptRequest):
    try:
        result = service.rsa_encode(request.text, request.key)
        return CryptoResponse(result=result, algorithm="RSA-512", success=True)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/rsa/decode", response_model=CryptoResponse)
def rsa_decode(request: DecryptRequest):
    try:
        result = service.rsa_decode(request.text, request.key)
        return CryptoResponse(result=result, algorithm="RSA-512", success=True)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))