# ---------- 1️⃣ Base Image ----------
FROM python:3.10-slim AS base

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# ---------- 2️⃣ Set Working Directory ----------
WORKDIR /app

# ---------- 3️⃣ System Dependencies ----------
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc curl && \
    rm -rf /var/lib/apt/lists/*

# ---------- 4️⃣ Copy Dependency Files First ----------
COPY requirements.txt .

# ---------- 5️⃣ Install Dependencies ----------
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    python -m spacy download en_core_web_md --direct

# ---------- 6️⃣ Copy Source Code ----------
COPY . .

# ---------- 7️⃣ Expose Port ----------
EXPOSE 5000

# ---------- 8️⃣ Run App with Gunicorn ----------
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
