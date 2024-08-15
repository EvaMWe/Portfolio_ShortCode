import tkinter as tk
from tkinter import ttk

import ttkbootstrap as ttkb

# TODO
#modify the logic behint the check botton, not properly functioning since after pressing multple times it get disabled forever

class SetDelButton:
    def __init__(self,frame):
        self.frame = frame
        self.del_button = ttkb.Button(self.frame, bootstyle="danger", text="delete")
        self.del_button.grid(column=3, row=0, padx=20, pady=5)
        self.del_button.bind("<ButtonRelease-1>", self.del_button_event)

    def del_button_event(self):
        if self.del_button.winfo_exists():
            self.del_button.grid_forget()


class TaskCombo:
    def __init__(self, frame):
        self.task_frame = ttk.Frame(frame, width = 450, height = 50)  #masterwidget
        self.task_frame.pack(fill=tk.BOTH, expand=True)
        self.add_button = None
        self.del_button = None
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





    def check_entry_text(self, event=None):
        self.task_field.unbind_all("<ButtonRelease-1>")
        if self.task_field.get():
            print("irgendwas")
            self.add_button = ttkb.Button(self.task_frame, bootstyle="success", text="add task")
            self.add_button.grid(column=3, row=1, padx=20, pady=5)
            self.add_button.focus_set()
            self.add_button.bind("<ButtonRelease-1>", self.add_button_event)
            self.text_written = True
            self.checkbutton.config(state = "enabled")
        else:
            self.text_written = False
            self.checkbutton.config(state="disabled")
            if self.del_button is not None:
                self.del_button.grid_forget()
            print("etwas anderes")
            # if self.add_b != None:
            #     self.add_b.destroy


    #Events
    def add_button_event(self, event=None):
        print("here goes further")

    def add_button_destroy(self):
        self.add_button.grid_forget()



    def checkbox_event(self, event):
        print("Wert des Check_bottons davor: ", self.check_var.get())
        if self.check_var.get() == False and self.text_written:
        #     #self.check_var.set(True)
            self.task_field.configure(state = "disable")
            self.checkbutton.configure(state = "normal")
        #create a delete button:
            self.del_button = ttkb.Button(self.task_frame, bootstyle="danger", text="delete")
            self.del_button.grid(column=3, row=0, padx=20, pady=5)
            self.del_button.focus_set()

        elif self.check_var.get() == True:
        #     #self.check_var.set(False)
        #     self.task_frame.update_idletasks()
        #     self.checkbutton.update_idletasks()
            self.task_field.configure(state="normal")
            print("2.condition entered:", self.check_var.get(), self.task_field.get())


class main_body:
    root = ttkb.Window(themename="superhero")
    root.title("My to Dos")
    root.geometry("500x800")
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

    test = TaskCombo(middle_frame)

    # task_list = []
    # task_list.append(TaskCombo(main_frame))

    root.mainloop()


if __name__ == "__main__":
    main_body()

