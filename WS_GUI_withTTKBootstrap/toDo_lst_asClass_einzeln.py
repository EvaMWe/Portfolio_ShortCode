import tkinter as tk
from tkinter import ttk

import ttkbootstrap as ttkb

# TODO
# bind this into a list, and do the same thing with all the other TaskCombi INstances created on pressing add button
# implement the deletion of a TaskCombo on pressing the del button, delete it from list; indices?
# condition: on empty Task Combo is the minimum content in the To Do list (widget cannot be empty)


class SetAddButton:
    ''' class to create the add button, including a function that will preform deleting the button'''
    def __init__(self,frame):
        self.frame = frame
        self.add_button = ttkb.Button(self.frame, bootstyle="success", text="add task")
        self.add_button.grid(column=3, row=1, padx=20, pady=5)
        self.add_button.focus_set()
        self.add_button.bind("<ButtonRelease-1>", self.add_button_event)

    def add_button_destroy(self):
        self.add_button.grid_forget()

    def add_button_event(self, event):
        '''create a new task'''
        main_body.creat_taskCombo()



class SetDelButton:
    def __init__(self,frame):
        self.frame = frame
        self.del_button = ttkb.Button(self.frame, bootstyle="danger", text="delete")
        self.del_button.grid(column=3, row=0, padx=20, pady=5)
        self.del_button.bind("<ButtonRelease-1>", self.del_button_event)

    def del_button_event(self):
        if self.del_button.winfo_exists():
            self.del_button.grid_forget()


class TaskField:
    def __init__(self,frame):
        self.add_b = None
        self.frame = frame
        self.entry_task = ttkb.Entry(self.frame, width=50)
        self.entry_task.grid(column=1, row=0, padx=20)
        self.entry_task.bind("<Return>", lambda event=None: self.check_entry_text(self))
        self.entry_task.bind_all("<ButtonRelease-1>", lambda event: self.check_entry_text(event))

    def configure(self, cur_state ="active"):
        self.entry_task.configure(state = cur_state)

    #check if something is written on event: Return
    def check_entry_text(self, event=None):
        if self.entry_task.get():
            self.written = True
            self.add_b = SetAddButton(self.frame)
        else:
            self.written = False
            if self.add_b != None:
                self.add_b.destroy



class CheckButton:
    def __init__(self,*args):  #*args: masterwidget
        self.add_button = None
        #checkbutton
        self.check_var = tk.IntVar()
        self.frame = args[0]
        self.checkbutton = ttkb.Checkbutton(args[0], variable=self.check_var)
        self.checkbutton.grid(column=0, row=0, sticky="w")
        self.checkbutton.bind("<ButtonRelease-1>", lambda event: self.checkbox_clicked(written=True))
        if len(args) == 2:
            self.obj_del = args[1]   #textfeld

    def checkbox_clicked(self,  written=True):
        #print("Existiert ein del button: ", self.del_b)
        if written == True and self.check_var.get() == 0:
            self.obj_del.configure("disable")
            self.del_b = SetDelButton(self.frame)

        else:
            self.obj_del.configure("active")  #activate text entry
            self.del_b.del_button_event()  #delete delete button


class TaskCombo: #this is the widget containing all the tasks;
    def __init__(self, frame):
        self.task_frame = ttk.Frame(frame, width = 450, height = 50)  #masterwidget
        self.task_frame.pack(fill=tk.BOTH, expand=True)
        self.task_field = TaskField(self.task_frame)
        self.check_box = CheckButton(self.task_frame, self.task_field)  #textfeld
        self.add_button = None
        self.del_button = None


class main_body:

    #classattributes, always the same
    root = ttkb.Window(themename="superhero")
    root.title("My to Dos")
    root.geometry("500x800")
    #create a main frame
        # self.main_frame = ttkb.Frame(self.root)
        # self.main_frame.pack(padx=10, pady=10)

    #create a top frame onto the root
    top_frame = ttkb.Frame(root)
    top_frame.pack(padx=10, pady=10)

    #create a label in the top frame
    label = ttkb.Label(top_frame, text="My To Do List", font=("Arial", 18), bootstyle="danger")
    label.pack(pady=50, padx=30)  # 50 von oben/unten, 30 von rechts/links

    #create a middle frame
    middle_frame = ttkb.Frame(root)
    middle_frame.pack(padx=3, pady=3)

    test = TaskCombo(middle_frame)

    # task_list = []
    # task_frame_list = []
    #
    # task_frame_list.append(ttkb.Frame(middle_frame))
    # task_frame_list.append(ttkb.Frame(middle_frame))
    #
    # for i in range(len(task_frame_list)):
    #     task_frame_list[i].pack(padx=10, pady=10)
    #     task_list.append(TaskCombo(task_frame_list[i]))

    root.mainloop()


if __name__ == "__main__":
    main_body()

