# AI Mini-Planning Agent
A Python agent that analyzes a list of tasks, prioritizes them, and generates a weekly plan using an LLM (Groq + LLaMA 3.3 70B).

## Project Structure
```
mini-planning-agent/
├── main.py                   # Entry point
├── tasks.py                  # Input task list
├── requirements.txt
├── .env.example              # Environment variables template
├── weekly_plan.txt           # Generated upon execution (do not upload to git)
└── src/
    ├── agents/
    │   └── agent.py          # PlanningAgent — calls the LLM
    ├── models/
    │   └── task.py           # Task Class — data model
    └── utils/
        └── file_handler.py   # Save and read the generated plan
```

## Installation

1. Clone the repository and enter the folder:
```bash
git clone <repo-url>
cd planning_agent
```

2. Create a virtual environment and install dependencies::
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Get your GROQ API key:
```bash
https://console.groq.com/keys
```

4. Configure your Groq API key:
```bash
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

## Usage
```bash
python main.py
```

The result is printed to the console and automatically saved in `weekly_planning.txt`.

## Design Decisions

- **`tasks.py` separate**: Makes it easier to change the data source without touching the core logic.
- **`PlanningAgent` as a class**: Allows for future expansion with memory or multiple agents.
- **`file_handler.py` separate**: Single Responsibility Principle — the agent knows nothing about files.
- **`temperature=0.3`**: More deterministic and consistent responses in the output format.
- **Separate System prompt + user prompt**: Better control over the model's behavior.