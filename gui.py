import functions
import PySimpleGUI as sg
import time

sg.theme('Black')
clock = sg.Text('', key='clock')
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a To-Do", key='todo', size=[47, 10])
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window("My To-Do App",
                   layout=[[label], [clock],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 10))

while True:
    event, value = window.read(timeout=80)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            if len(value['todo']) == 0:
                continue
            else:
                todos = functions.get_todos()
                new_todo = value['todo'] + '\n'
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = value['todos'][0]
                new_todo = value['todo']+'\n'

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item to edit ", font=('Helvetica', 10))

        case "todos":
            try:
                window['todo'].update(value=value['todos'][0].strip('\n'))
            except IndexError:
                sg.popup("Add an item to select", font=('Helvetica', 10))

        case "Complete":
            try:
                todo_to_complete = value['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item ", font=('Helvetica', 10))

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()
