# OSINT Cyber Intelligence Platform

This repository is now organized as a **Codex-friendly modular project** with backend services, investigation modules, dataset files, and a starter frontend folder.

## Project Layout

```text
backend/
  api/main.py                  FastAPI entrypoint
  scanners/username_scanner.py Async username scanner
  ai/planner.py                Investigation planning logic
  ai/agent.py                  Orchestrates end-to-end investigation
  ai/entity_extractor.py       Email extraction helper
  ai/correlation.py            Identity confidence scoring
  ai/threat_scoring.py         Threat scoring engine
  graph/graph_engine.py        Intelligence graph builder
  datasets/sites.json          OSINT site dataset

frontend/src/
  App.jsx
  Graph.jsx

osint_platform.py              Simple CLI runner
osint_cyber_intelligence.py    Backward-compatible CLI runner
requirements.txt
```

## Install

```bash
pip install -r requirements.txt
```

## Run CLI

```bash
python3 osint_platform.py
```

## Run API

```bash
uvicorn backend.api.main:app --reload
```

Open API docs at: `http://127.0.0.1:8000/docs`

## Codex in VS Code

To continue building this project with Codex in VS Code:
1. Install the OpenAI Codex extension.
2. Open this repository in VS Code.
3. Use prompts like:
   - "Add Neo4j persistence to graph engine"
   - "Add React graph visualization and API integration"
   - "Expand sites dataset and add per-site detection rules"
