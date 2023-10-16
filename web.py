import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("To-Do App")
st.subheader("Welcome to my todo app")
st.write("This app is to increase your productivity :)")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a Todo",label_visibility='hidden',
              placeholder="Add a Todo...",
              on_change=add_todo, key='new_todo')

st.session_state
