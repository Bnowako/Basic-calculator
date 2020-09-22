from tkinter import *
from tkinter import ttk
from main import Calc_Handler

result = 0
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
operations = ["/", "x", "-", "+"]
operation_dict = {"a_value": "", "b_value": "",
                  "operation_type": "", "erase_label_text": False}
calc_handler = Calc_Handler()


def reset_operation():
    operation_dict["a_value"] = ""
    operation_dict["b_value"] = ""
    operation_dict["operation_type"] = ""
    operation_dict["erase_label_text"] = False


def handle_number_press(button):
    # Zostaje wywolana za kazdym razem jak jest wcisniety przycisk
    # 1. Wpisywanie zwykłe DONE
    # 2. Wpisywanie po kolejnej operacji +,/,*,- DONE
    # 3. Wpisywanie po otrzymaniu wyniku = DONE
    global operation_dict
    if operation_dict["erase_label_text"]:
        result.set("")
        operation_dict["erase_label_text"] = False
    result.set(result.get()+button)


def handle_ac_press():
    # Resetuje wszystkie ustawienia
    result.set("")
    reset_operation()


def handle_operation_press(button):
    # 1. Nie wpisano zadnej liczby
    # 2. Zostala wprowadzona a_value, nie ma jeszcze b
    # 3. Zostala wykonana juz jedna operacja, powinna byc ustawiona jako a_value

    if operation_dict["a_value"] == "":
        operation_dict["a_value"] = result.get()
        result.set("0")
        operation_dict["operation_type"] = button
        operation_dict["erase_label_text"] = True

    elif operation_dict["a_value"] != "":
        operation_dict["b_value"] = result.get()
        temp_a_value = calc_handler.input_handler(operation_dict)
        reset_operation()
        operation_dict["a_value"] = temp_a_value
        operation_dict["operation_type"] = button
        operation_dict["erase_label_text"] = True
        result.set(operation_dict["a_value"])


def handle_result_press():
    # Pokazuje wynik i resetuje aplikacje

    if operation_dict["a_value"] != "":
        operation_dict["b_value"] = result.get()
    if operation_dict["a_value"] != "" and operation_dict["b_value"] != "":
        temp_a_value = calc_handler.input_handler(operation_dict)
        reset_operation()
        operation_dict["erase_label_text"] = True
        result.set(temp_a_value)


def onClick(button):
    if button in numbers:
        handle_number_press(button)
    elif button == "AC":
        handle_ac_press()
    elif button in operations:
        handle_operation_press(button)
    elif button == "=":
        handle_result_press()


def initialize_window():
    global result
    root = Tk()
    result = StringVar()
    result.set("")
    root.title("Calculator")

    l = Label(root, textvariable=result, pady=15)
    l.grid(column=0, row=0, columnspan=4)

    buttons = [["AC", " ", " ", "/"], ["7", "8", "9", "x"],
               ["4", "5", "6", "-"], ["1", "2", "3", "+"], ["0", ".", "=", "="]]
    buttons_dict = {}

    for i, rows in enumerate(buttons):
        i += 1
        for j, button in enumerate(rows):
            buttons_dict[f'b{i}.{j}'] = Button(
                root, command=lambda button=button: onClick(button), text=button, padx=15, pady=15)
            buttons_dict[f'b{i}.{j}'].grid(column=j, row=i)
    root.mainloop()


initialize_window()
