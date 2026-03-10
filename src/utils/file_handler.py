# Utils for saving and reading the generated plan

OUTPUT_FILE = "weekly_planning.txt"

def save_plan(content: str, filepath: str = OUTPUT_FILE):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\nPlanning saved in: '{filepath}'")

def load_plan(filepath: str = OUTPUT_FILE):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()