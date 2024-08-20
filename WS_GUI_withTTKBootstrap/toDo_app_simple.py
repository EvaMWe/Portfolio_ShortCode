import tkinter as tk
from tkinter import ttk

import ttkbootstrap as ttkb


# TODO
# initialize the buttons from the beginning on
# put delete and add button next to each other
# default status of buttons: disabled or invisible (Is that passible?)

# give a maximum number of characters and fix the size (should be visualized more static)
# check all the functions
# check always if TaskCombo is the last one that is deleted or create automatically a new one, if side is empty


class TaskCombo:
    def __init__(self, master_frame):
        self.task_frame = ttk.Frame(master_frame, width=450, height=50)  #masterwidget
        self.task_frame.pack(fill=tk.BOTH, expand=True, padx=4, pady=10)

        #text field
        self.task_field = ttkb.Entry(self.task_frame, width=50)
        self.task_field.grid(column=1, row=0, padx=4)
        self.task_field.bind("<Return>", lambda event=None: self.check_entry_text(event))
       # self.task_field.bind("<ButtonRelease-1>", lambda event=None: self.check_entry_text(event) if event.widget == self.task_field else None)
        self.text_written = False
        #check button
        #self.checkbutton_state = "disabled"
        self.check_var = tk.BooleanVar()
        self.checkbutton = ttkb.Checkbutton(self.task_frame, variable=self.check_var, state="disabled")
        self.checkbutton.grid(column=0, row=0, sticky="w")
        self.checkbutton.bind("<Button-1>", lambda event: self.checkbox_event(event))
        #add_button
        self.add_button = ttkb.Button(self.task_frame, bootstyle="success", text="add", width=4, state="disabled")
        self.add_button.grid(column=3, row=0, padx=4, pady=5)
        self.add_button.bind("<ButtonRelease-1>", self.add_button_event)
        #del_button
        self.del_button = ttkb.Button(self.task_frame, bootstyle="danger", text="x", width=4, state="disabled")
        self.del_button.grid(column=4, row=0, padx=4, pady=5)
        self.del_button.bind("<ButtonRelease-1>", self.del_button_event)



    # Events
    def check_entry_text(self, event=None):
        if self.task_field.get():
            print("irgendwas")
            self.checkbutton.config(state="enabled")
            self.add_button.focus_set()
            self.add_button.config(state="active")
        else:
            self.checkbutton.config(state="disabled")
        self.task_field.unbind_all("<ButtonRelease-1>")
            # if self.add_b != None:
            #     self.add_b.destroy

    def add_button_event(self, event=None):
        print("status of button:", self.add_button.cget("state"))
        if self.add_button.cget("state") == "active":
            toDo_app.create_new_combo()


    def del_button_event(self, event=None):
        print("status of button:", self.del_button.cget("state"))
        if self.del_button.cget("state") == "active":
            self.task_frame.destroy()
            toDo_app.del_combo(self)

    def checkbox_event(self, event):
        print("Wert des Check_bottons davor: ", self.check_var.get())
        if self.check_var.get() == False and self.task_field.get():
            #     #self.check_var.set(True)
            self.task_field.configure(state="disable")
            self.del_button.config(state="active")
        elif self.check_var.get() == True:
            self.task_field.configure(state="normal")
            print("2.condition entered:", self.check_var.get(), self.task_field.get())




class MainBody:
    def __init__(self, root):
        self.root = root
        self.root.title("My to Dos")
        self.root.geometry("500x800")
    #create a main frame
        self.main_frame = ttkb.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)

    #create a top frame
        self.top_frame = ttkb.Frame(self.main_frame)
        self.top_frame.pack(padx=10, pady=10)

    #create a label in the top frame
        self.label = ttkb.Label(self.top_frame, text="My To Do List", font=("Arial", 18), bootstyle="danger")
        self.label.pack(pady=50, padx=30)  # 50 von oben/unten, 30 von rechts/links

    #create a middle frame
        self.middle_frame = ttkb.Frame(self.main_frame)
        self.middle_frame.pack(padx=3, pady=3)
        self.task_combo_list = [TaskCombo(self.middle_frame)]


    def create_new_combo(self):
        self.task_combo_list.append(TaskCombo(self.middle_frame))
        print(self.task_combo_list)

    def del_combo(self, currTask):
        print(self.task_combo_list)
        print("current Task: ", currTask)
        self.task_combo_list.remove(currTask)
        if len(self.task_combo_list) == 0:
            self.task_combo_list.append(TaskCombo(self.middle_frame))





if __name__ == "__main__":
    root = ttkb.Window(themename="superhero")
    toDo_app = MainBody(root)
    root.mainloop()
