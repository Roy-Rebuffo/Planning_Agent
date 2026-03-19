# prompts/planner_prompt.py
# Defines the system and human prompts for the planning agent.
# System prompt sets the role and behaviour.
# Human prompt sends the task data to analyse.

from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

# Who the agent is and how it behaves
SYSTEM_TEMPLATE = SystemMessagePromptTemplate.from_template("""
You are an expert task planning assistant.
Your job is to analyse a list of tasks and generate a clear weekly plan.

Prioritisation criteria:
- The shorter the deadline, the higher the priority.
- If two tasks have the same deadline, prioritise the one with the longer duration.

Always respond in Spanish and follow the exact format specified by the user.
"""
)
# What the user sends — {tasks} will be replaced with the real task list
HUMAN_TEMPLATE = HumanMessagePromptTemplate.from_template("""
Analyse the following tasks and generate a weekly plan.

Tasks:
{tasks}

Respond EXACTLY in this format, without any extra text before or after:

Prioridad:
1. [tarea]
2. [tarea]
3. [tarea]

Plan semanal:
Lunes: [tarea]
Martes: [tarea]
Miércoles: [tarea]
Jueves: [tarea]
Viernes: [tarea]

Razón:
[Briefly explain why you assigned that priority and order]
"""
)
# Combine both into a single prompt template
CHAT_PROMPT = ChatPromptTemplate.from_messages([
    SYSTEM_TEMPLATE,
    HUMAN_TEMPLATE
])

def create_system_prompt():
    return CHAT_PROMPT