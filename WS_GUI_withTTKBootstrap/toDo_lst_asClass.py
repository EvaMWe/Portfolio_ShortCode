import tkinter as tk
from tkinter import ttk

import ttkbootstrap as ttkb


class SetAddButton:
    def __init__(self):
        self.add_button = ttkb.Button(middle_frame, bootstyle="success", text="add task")
        self.add_button.grid(column=3, row=1, padx=20, pady=5)
        self.add_button.focus_set()
        self.add_button.bind("<ButtonRelease-1>", self.add_button_event)

    def add_button_event(self):
        self.add_button.grid_forget()



class SetDelButton:
    def __init__(self):
        self.del_button = ttkb.Button(middle_frame, bootstyle="danger", text="delete")
        self.del_button.grid(column=3, row=0, padx=20, pady=5)
        self.del_button.bind("<ButtonRelease-1>", self.del_button_event)

    def del_button_event(self):
        if self.del_button.winfo_exists():
            self.del_button.grid_forget()



    # self.add_button.focus_set()


class CheckEntryCombo:
    def __init__(self):
        self.add_button = None
        #checkbutton
        self.check_var = tk.IntVar()
        self.checkbutton = ttkb.Checkbutton(middle_frame, variable=self.check_var)
        self.checkbutton.bind("<ButtonRelease-1>", self.checkbox_clicked)
        self.checkbutton.grid(column=0, row=0, sticky="w")
        #entry button
        self.entry_task = ttkb.Entry(middle_frame, width=50)
        self.entry_task.grid(column=1, row=0, padx=20)
        self.entry_task.bind("<Return>", self.check_entry_text)
        #other buttons
        self.add_b = None
        self.del_b = None
        self.written = False

    def checkbox_clicked(self, event=None):
        print("Existiert ein del button: ", self.del_b)
        if self.written == True and self.check_var.get() == 0:
            self.entry_task.configure(state="disable")
            self.del_b = SetDelButton()
        else:
            self.entry_task.configure(state="active")
            self.del_b.del_button_event()

     #check if something is written inside entry
    def check_entry_text(self, event=None):
        if self.entry_task.get():
            self.written = True
            print(self.written)
            self.add_b = SetAddButton()
            #print(self.written)
            #self.entry_task.after(10, lambda event=None: self.check_entry_text(self))
        else:
            self.written = False
            #print(self.written)
       # return self.written

    def checker(self):
        self.entry_task.bind("<Return>", lambda event: self.check_entry_text(event))

class TaskCombo:
    def __init__(self):
        self.frame = ttk.Frame(middle_frame)
        self.entry = CheckEntryCombo()

root = ttkb.Window(themename="superhero")
root.title("My to Dos")
root.geometry("500x350")
#create a main frame
main_frame = ttkb.Frame(root)
main_frame.pack(padx=10, pady=10)

#create a top frame
top_frame = ttkb.Frame(main_frame)
top_frame.pack(padx=10, pady=10)

#create a label in the top frame
label = ttkb.Label(top_frame, text="My To Do List", font=("Arial", 18), bootstyle="danger")
label.pack(pady=50, padx=30)  # 50 von oben/unten, 30 von rechts/links

#create a middle frame
middle_frame = ttkb.Frame(main_frame)
middle_frame.pack(padx=3, pady=3)


if __name__ == "__main__":

    root.mainloop()
