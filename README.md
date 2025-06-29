# Blood Test Report Analyzer

## Overview

A quirky AI-powered FastAPI application that analyzes blood test reports (PDFs) using a team of humorous and dramatized agents. The agents are designed using [CrewAI](https://docs.crewai.com/) and leverage local models via Ollama.

## Features

* Funny, over-the-top doctor, nutritionist, and fitness agents
* PDF blood report reading and parsing
* Local LLM integration with Ollama (e.g., Gemma 2B)
* Nutrition and exercise recommendations (satirical and not real medical advice)
* Swagger UI to interact with API
* Database integration to store user query and report analysis results

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ShivamShrivastava18/blood-test-analyzer.git
cd blood-test-analyzer
```

### 2. Create Virtual Environment

```bash
python -m venv wing
source wing/Scripts/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run Ollama (Gemma:2b)

```bash
ollama run gemma:2b
```

Make sure the Ollama server is running at `http://localhost:11434`

### 5. Create Database Tables

```bash
python create_tables.py
```

### 6. Start FastAPI Server

```bash
uvicorn main:app --reload
```

Now visit: [http://localhost:8000/docs](http://localhost:8000/docs) for the Swagger UI

## API Endpoints

### `GET /`

**Description:** Health check

**Response:**

```json
{
  "message": "Blood Test Report Analyser API is running"
}
```

### `POST /analyze`

**Description:** Analyze the uploaded blood test PDF using all agents

**Request Form Data:**

* `file`: PDF file (Upload)
* `query`: (Optional) Natural language prompt (default: "Summarise my Blood Test Report")

**Response:**

```json
{
  "status": "success",
  "query": "Summarise my Blood Test Report",
  "analysis": "... agent response ...",
  "file_processed": "uploaded_filename.pdf"
}
```

## Folder Structure

```
.
├── agents.py             # Defines the 4 CrewAI agents
├── task.py               # Defines the 4 CrewAI tasks
├── tools.py              # Blood report tool and mock tools
├── main.py               # FastAPI app entry point
├── database.py           # Database configuration
├── models.py             # Database models
├── create_tables.py      # Database table creation script
├── data/                 # Folder to temporarily store PDFs
├── requirements.txt
└── README.md
```

## Notes

* This app is intended for debugging, experimentation, and satire. It is **not** intended for real medical use.
* The agents make exaggerated or fictional suggestions for illustrative and entertainment purposes.

## License

MIT License
