# Python 3.11 — biz tanlagan versiya
FROM python:3.11-slim

# Container ichida ishchi papka
WORKDIR /app

# Avval requirements ko'chiramiz va o'rnatamiz
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Qolgan fayllarni ko'chiramiz
COPY . .

# Portni ochish
EXPOSE 8000

# Ishga tushirish buyrug'i
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
