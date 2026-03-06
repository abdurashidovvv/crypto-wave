from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import crypto

app = FastAPI(
    title="CryptoWave API",
    version="1.0.0",
    docs_url="/api/docs",       # ← docs manzilini o'zgartirdik
    openapi_url="/api/openapi.json"
)

# CORS — React frontend bilan gaplashishi uchun kerak
# (keyingi bosqichlarda tushuntiramiz)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routerni ulash
app.include_router(crypto.router)

# Sog'liqni tekshirish uchun oddiy endpoint
@app.get("/api/health")
def health():
    return {"status": "ok"}
