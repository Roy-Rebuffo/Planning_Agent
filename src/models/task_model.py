from pydantic import BaseModel, Field

class TaskAnalysis(BaseModel):
    """Individual task written by the user"""

    task_name: str = Field(description="Name of the given task")
    deadline_days: int = Field(description="Number of days left to finish the task")
    duration_days: int = Field(description="Number of days the task will take to complete")