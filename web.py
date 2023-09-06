import streamlit
import functions

todos = functions.get_todos()

def add_todo(): 
    todo = streamlit.session_state["inputbox"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

streamlit.title('Todo.')
streamlit.subheader('All your tasks in one place:')

for index , todo in enumerate(todos):
    checkbox = streamlit.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del streamlit.session_state[todo]
        streamlit.experimental_rerun()


streamlit.text_input(label="", placeholder='Add or Edit todo', 
                     on_change= add_todo, key='inputbox')
