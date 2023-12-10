import streamlit as st
import functions

todos = functions.getToDos()
def addTodo():
    todo = st.session_state["newTodo"] + '\n'
    todos.append(todo)
    functions.setToDos(todos)

st.title("My Todo App")
st.subheader("Testing")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.setToDos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" ", placeholder="Add a new todo",
              on_change=addTodo, key="newTodo")
