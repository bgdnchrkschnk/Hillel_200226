FROM python:3.9-slim

WORKDIR /app

# копіюємо requirements.txt
COPY requirements.txt .

# ставимо системні пакети для psycopg2
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# встановлюємо Python-залежності
RUN pip install --no-cache-dir -r requirements.txt

# копіюємо всі файли з директорії tests/docker
COPY . .

# запускаємо всі тести у цій директорії
CMD ["pytest"]