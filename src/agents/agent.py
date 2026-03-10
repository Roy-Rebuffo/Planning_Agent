# Planning agent that connects to Groq and builds the prompt and replies with the planning
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class PlanningAgent:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env module")
        self.client = Groq(api_key = api_key)
        self.model = "llama-3.3-70b-versatile"

    def build_prompt(self, tasks: list[dict]):
        task_lines = "\n".join(
            f"- {t['task']}: ends in {t['deadline_days']} days, "
            f"estimated time {t['duration']} hours"
            for t in tasks
        )

        return f"""You are a task planning assistant
        Analyse the following list of tasks and generate a weekly plan in Spanish.

        Tasks:
        {task_lines}

        Prioritisation criteria:
        - The shorter the deadline, the higher the priority.
        - If two tasks have the same deadline, prioritise the one with the longer duration.

        Respond EXACTLY in this format, without any extra text before or after:

        Priority:
        1. [task]
        2. [task]
        3. [task]

        Weekly plan:
        Monday: [task]
        Tuesday: [task]
        Wednesday: [task]
        Thursday: [task]
        Friday: [task]

        Reason:
        [Briefly explain why you have assigned that priority and order in the plan]
        """
    def run(self, tasks: list[dict]):
        prompt = self.build_prompt(tasks)

        response = self.client.chat.completions.create(
            model = self.model,
            messages = [
                {
                    "role": "system",
                    "content": "You are a planning assistant. You always respond in Spanish and follow the specified format."
                },
                {
                    "role": "user",
                    "content": prompt
                },
            ],
            temperature = 0.3,
        )

        return response.choices[0].message.content