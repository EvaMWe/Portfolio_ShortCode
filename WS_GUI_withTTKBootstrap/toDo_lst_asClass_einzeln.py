import tkinter as tk
from tkinter import ttk
import sqlite3

import ttkbootstrap as ttkb


# TODO
# add a new TaskCombo on clicking on the add button
# delete the TaskCombo on clicking on the del button

class conn_database:
    def __init__(self):

        self.db_name = "datastore_todo"
        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()  # Der Cursor wird erstellt

        #create the task table if not yet existing:
    def create_task_table(self):
        sql = """CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_name TEXT NOT NULL,
                    task_status TEXT NOT NULL);"""
        self.c.execute(sql)
        self.conn.commit()
        self.conn.close()



class TaskCombo:
    def __init__(self, master_frame):
        self.task_frame = ttk.Frame(master_frame, width=450, height=50)  #masterwidget
        self.task_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=10)

        #text field
        self.task_field = ttkb.Entry(self.task_frame, width=50)
        self.task_field.grid(column=1, row=0, padx=20)
        self.task_field.bind("<Return>", lambda event=None: self.check_entry_text(event))
        self.task_field.bind_all("<ButtonRelease-1>", lambda event=None: self.check_entry_text(event))
        self.text_written = False
        #check button
        #self.checkbutton_state = "disabled"
        self.check_var = tk.BooleanVar()
        self.checkbutton = ttkb.Checkbutton(self.task_frame, variable=self.check_var, state="disabled")
        self.checkbutton.grid(column=0, row=0, sticky="w")
        self.checkbutton.bind("<Button-1>", lambda event: self.checkbox_event(event))
        self.add_button = None
        self.del_button = None

    # Events
    def check_entry_text(self, event=None):
        self.task_field.unbind_all("<ButtonRelease-1>")
        if self.task_field.get():
            print("irgendwas")
            self.add_button = ttkb.Button(self.task_frame, bootstyle="success", text="add task")
            self.add_button.grid(column=3, row=1, padx=20, pady=5)
            self.add_button.focus_set()
            self.add_button.bind("<ButtonRelease-1>", self.add_button_event)
            self.text_written = True
            self.checkbutton.config(state="enabled")
        else:
            self.text_written = False
            self.checkbutton.config(state="disabled")
            #remove the del button if one exists
            if self.del_button is not None:
                self.del_button.grid_forget()
            print("etwas anderes")
            # if self.add_b != None:
            #     self.add_b.destroy

    def add_button_event(self, event=None):
        toDo_app.create_new_combo()
        self.add_button.grid_forget()

    def checkbox_event(self, event):
        print("Wert des Check_bottons davor: ", self.check_var.get())
        if self.check_var.get() == False and self.text_written:
            #     #self.check_var.set(True)
            self.task_field.configure(state="disable")
            self.checkbutton.configure(state="normal")
            #create a delete button:
            self.del_button = ttkb.Button(self.task_frame, bootstyle="danger", text="delete")
            self.del_button.grid(column=3, row=0, padx=20, pady=5)
            self.del_button.focus_set()
            self.del_button.bind("<ButtonRelease-1>", self.del_button_event)

        elif self.check_var.get() == True:
            self.task_field.configure(state="normal")
            print("2.condition entered:", self.check_var.get(), self.task_field.get())

    def del_button_event(self, event=None):
        self.task_frame.destroy()



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

    # task_list = []
    # task_list.append(TaskCombo(main_frame))




if __name__ == "__main__":
    root = ttkb.Window(themename="superhero")
    db = conn_database()
    db.create_task_table()
    toDo_app = MainBody(root)
    root.mainloop()
