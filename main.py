# Entry point
# WorkFlow: load tasks -> call agent -> display result -> save to file

from tasks import TASKS
from src.agents.agent import PlanningAgent
from src.utils.file_handler import save_plan

def main():
    print("Starting building agent...\n")

    agent = PlanningAgent()

    print(f"Incomming tasks: {len(TASKS)}")

    for t in TASKS:
        print(f"   - {t['task']}  (deadline:  {t['deadline_days']} days, duration:  {t['duration']}hrs)")
    
    print("\n Analysing tasks...")
    result = agent.run(TASKS)

    print("=" * 50)
    print(result)
    print("=" * 50)

    save_plan(result)

if __name__ == "__main__":
    main()