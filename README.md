# 🌴 Caribbean AI Kitchen

An AI-powered recipe generator that uses **Gemini 2.5 Flash** to create authentic Caribbean recipes and **Aerospike** for low-latency storage. Features high-performance filtering using **Aerospike Secondary Indexes**.

## 🚀 Features
- **AI Generation:** Uses Gemini 2.5 Flash with "Thinking" reasoning for culinary expertise.
- **Fast Storage:** Built on Aerospike Community Edition.
- **Secondary Indexing:** Instant filtering by island (e.g., Jamaica, Haiti, Trinidad).
- **Dockerized:** One-command deployment using Docker Compose.

## 🛠 Tech Stack
- **Frontend:** Streamlit
- **Database:** Aerospike CE (v8.1+)
- **AI Engine:** Google Gemini 2.5 Flash
- **Orchestration:** Docker Compose

## 🚦 Quick Start

### 1. Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed.
- A Google Gemini API Key from [AI Studio](https://aistudio.google.com/).

### 2. Configuration
Create a `.env` file in the root directory:
```text
GEMINI_API_KEY=your_api_key_here
AEROSPIKE_HOST=aerospike
```
### 3. Docker compose build:
```text
docker compose up --build
```

## 📁 Project Structure
- **app/app.py:** The Streamlit application logic.
- **app/Dockerfile:** Container configuration for the Python environment.
- **docker-compose.yml:** Multi-container orchestration (Database + UI).
- **aerospike_data/:** Persistent storage volume for your recipes.
