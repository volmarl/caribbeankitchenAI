FROM python:3.9-slim

# Install system dependencies for Aerospike C-based client
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libyaml-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

EXPOSE 8501

# Entry point starts Streamlit directly
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
