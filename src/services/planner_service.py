# Connects the prompt with Groq LLM using LangChain
# Receives a list of TaskAnalysis, formats them and returns the generated plan

import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from models.task_model import TaskAnalysis
from prompts.planner_prompts import create_system_prompt

load_dotenv()

def format_tasks(tasks: list[TaskAnalysis]) -> str:
    """Converts a list of TasksAnalysis into readable text for the prompt"""

    lines = []

    for task in tasks:
        line = f"- {task.task_name}: {task.deadline_days} days left, takes {task.duration_days} days"
        lines.append(line)

    return "\n".join(lines)

def generate_plan(tasks: list[TaskAnalysis]) -> str:
    """Calls the LLM with the task list and returns the weekly plan."""

    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.3-70b-versatile",
        temperature=0.3,
    )

    prompt = create_system_prompt()

    # LangChain chain: prompt -> llm -> output

    chain = prompt | llm

    response = chain.invoke({"tasks": format_tasks(tasks)})

    return response.content