import streamlit as st
# app title
st.title("TO-DO List App")
# installation session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []
# sidebar heading
st.sidebar.header("Manage Your Task")

# text input
new_task = st.sidebar.text_input("Add a new task:", placeholder="Enter your task here...")

if st.sidebar.button("Add Task"):
    if new_task.strip():
        st.session_state.tasks.append({"task":new_task, "completed":False})
        st.success("Task added successfully!")
    else:
        st.warning("Task cannot be empty!")

# display tasks
st.subheader("Your TO-DO List")
if not st.session_state.tasks:
    st.info("No task added yet start by adding a task from the sidebar")
else:
    for index, task in enumerate(st.session_state.tasks):
        col1 , col2 , col3 = st.columns([0.7, 0.15, 0.15])

        # mark as completed
        completed = col1.checkbox(f"**{task['task']}**",task["completed"],key=f"check_{index}")
        if completed != task["completed"]:
            st.session_state.tasks[index]["completed"] = completed


    # update task
    if col2.button("Edit",key=f"edit_{index}"):
        new_task = st.text_input("Edit Task",task["task"],key=f'edit_input_{index}')
        if new_task and st.button("save", key=f'save_{index}'):
            st.session_state.tasks[index]['task'] = new_task
            st.experimental_rerun()


    # delete task
    if col3.button("Delete",key=f"delete_{index}"):
        del st.session_state.tasks[index]
        st.experimental_rerun() 

# clear all tasks
if st.button("clear all tasks"):
    st.session_state.tasks = []
    st.success("All tasks deleted successfully")

# Footer
st.markdown('---')
st.caption("stay organized & procutive with this simple TO-DO List app")