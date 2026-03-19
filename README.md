# 🗓️ Planning Agent (Groq + LangChain)

An intelligent weekly planning agent that analyses a to-do list and generates a prioritised plan using AI.

## ✨ Features

- **Visual interface:** An interactive form created with Streamlit.
- **AI analysis:** Prioritises tasks and generates a weekly plan using LLaMA 3.3 70B via Groq.
- **Data validation:** Tasks are automatically validated with Pydantic.
- **Explained reasoning:** The agent explains why it has assigned each priority.

## 🛠️ Installation

1. **Clone the project:**
```bash
git clone <repo-url>
cd planning_agent
```

2. **Create and activate the virtual environment:**
```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure the API key:**
```bash
cp .env.example .env
# Edit .env and add your Groq API key
```

## 🚀 Usage
```bash
streamlit run main.py
```

1. Add your tasks with a name, days until the deadline and estimated duration.
2. Click **‘Generate plan’** and get your weekly plan with reasoning included.

## 📁 Project structure
```
planning_agent/
├── src/
│   ├── models/
|        └── task_model.py        # Data model with Pydantic
│   ├── prompts/
|        └── planner_prompts.py   # System and human prompts
│   ├── services/
|        └── planner_service.py   # Agent logic with LangChain + Groq
│   └── ui/
│       └── streamlit_ui.py       # User interface
├── main.py
├── .env.example
├── requirements.txt
└── venv/
```

## What would I improve if I had more time?

- Export the generated plan to a `.txt` or `.pdf` file
- Support for monthly planning when tasks span more than 7 days
- History of previous plans
- Unit tests
