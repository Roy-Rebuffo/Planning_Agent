#Representation task Model

class Task:
    def __init__(self, task: str, deadline_days: int, duration: int):
        self.task = task
        self.deadline_days = deadline_days
        self.duration = duration

    def __str__(self) -> str:
        return f"Tarea: {self.task} | Plazo: {self.deadline_days} días"
    
    #TODO study __repr__ for for better debuggs

    #TODO study to_dict for better representation of objects instead of dictionaries