# Streamlit interface for the task planning agent
# The user adds tasks one by one and generates a weekly plan

import streamlit as st
from models.task_model import TaskAnalysis
from services.planner_service import generate_plan

def run_app():
    st.title("Agente planificador de Tareas")
    st.write("Agrega tus tareas y genera tu plan semanal con IA")

    # Initialize the task list in session state if it doesnt exist yet
    # Session_state keeps data between interactions without reseting until refreshing page

    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    # ---FORM TO ADD A NEW TASK---
    st.subheader("Agrega una tarea")

    task_name = st.text_input("Nombre de la tarea")
    deadline_days = st.number_input("Días para que la tarea finalize", min_value=1, step=1)
    duration_days = st.number_input("Duración de la tarea en días", min_value=1, step=1)

    if st.button("Añadir tarea"):
        if task_name.strip() == "":
            st.warning("Por favor el introduzca nombre de la tarea")
        else:
            # Create a TaskAnalysis and validates with pydantic automatically
            new_task = TaskAnalysis(
                task_name=task_name,
                deadline_days=int(deadline_days),
                duration_days=int(duration_days),
            )
            st.session_state.tasks.append(new_task)
            st.success(f"Tarea {task_name} añadida con éxito!")
    
    # ---Show current task list---
    if st.session_state.tasks:
        st.subheader("Tareas hasta ahora...")
        for i, task in enumerate(st.session_state.tasks):
            st.write(f"{i + 1}. **{task.task_name}** — {task.deadline_days} días restantes, {task.duration_days} días para completar la tarea")

        # Generate plan button
        if st.button("Generar plan"):
            with st.spinner("Analizando el plan..."):
                result = generate_plan(st.session_state.tasks)

            st.subheader("📋 Tu plan semanal")
            st.text(result)