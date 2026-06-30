# 🧠 AI Resume Analyzer

An advanced, production-ready AI-powered Resume Analyzer built using **FastAPI** and the **Google Gemini Pro API (`gemini-2.5-flash`)**. This application parses resume data, extracts technical core competencies, performs dynamic skill-gap analytics against target job roles, and generates visual performance reports alongside actionable AI-driven career recommendations.

---

## 🚀 Key Features

* **Automated ATS Parsing:** Seamlessly extracts text from complex resume layouts using high-fidelity PDF extraction tools.
* **Deterministic Skill Extraction:** Leverages structured Google Gemini JSON schemas to pull objective technical competencies, minimizing hallucinations.
* **Dynamic Job Match Analytics:** Matches candidate skill sets against predefined benchmarks or dynamically fetches industry-standard criteria on-the-fly using LLMs.
* **Actionable Gap Analysis:** Computes real-time match scores and lists explicit missing skills.
* **Data Visualization:** Generates and encodes base64 visual competency charts using Matplotlib for seamless frontend rendering.
* **Contextual AI Mentorship:** Provides high-value strategic advice and structured learning paths based on the identified skill gaps.

---

## 🛠️ Tech Stack & Architecture

* **Backend Framework:** FastAPI (Asynchronous Python Web Framework)
* **LLM Orchestration:** Google GenAI SDK (`gemini-2.5-flash` with structured execution configs)
* **Data Visualization:** Matplotlib
* **Environment Management:** Python-Dotenv
* **Server Gateway:** Uvicorn (ASGI Server)

### 📊 System Workflow
1. **User Client:** Submits a Resume File (PDF) and target `job_role` via Multipart Form Data.
2. **FastAPI Engine:** Validates the payload and passes the file to the local pipeline engine.
3. **Gemini Utility Platform:** Extracts structured data from raw textual data using JSON schemas.
4. **Analytics Pipeline:** Evaluates skill arrays and returns match metrics along with dynamic Matplotlib analytical charts.
5. **Response Delivery:** Outputs a neat JSON payload containing comprehensive audit logs, visualization objects, and AI mentorship guidelines.

---

## 📂 Project Directory Structure

```text
ai-resume-analyzer-project/
├── main.py              # Main ASGI application & endpoint definitions
├── gemini_utils.py      # Structured Gemini API orchestration and configurations
├── model.py             # Advanced skill-gap analytics & calculation logic
├── utils.py             # PDF text extraction utilities
├── graph_utils.py       # Matplotlib visualization and base64 encoding pipeline
├── job_roles.py         # Static configurations for industry-standard tech stacks
├── requirements.txt     # Locked project dependencies
└── .env                 # Environment configuration file (Ignored in git)