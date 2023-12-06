from tkinter import *


def klikel_one_pluss():
    entry_one_klik = int(entry_value.get())
    entry_one_klik += 1
    entry_value.set(entry_one_klik)
    

def clear_text_entry():
    entry_value_clear = int(entry_value.get())
    entry_value_clear = 0
    entry_value.set(entry_value_clear)


root = Tk()
root.title("Кликер")
root.geometry("210x100")

frame = Frame(root, padx=35, pady=2)
frame.pack(expand=True, fill="both")

entry_value = StringVar()
entry_value.set("0")

entry = Entry(frame, width=9, justify='center', textvariable=entry_value)
entry.pack(pady=6)

bt_klikel = Button(frame, text="Клик", width=4, height=1, command=klikel_one_pluss)
bt_klikel.pack(side="left")
bt_clear = Button(frame, text="Сброс", width=4, height=1, command=clear_text_entry)
bt_clear.pack(side="right")

root.mainloop()
