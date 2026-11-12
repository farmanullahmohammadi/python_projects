
import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Advanced Student Profile")
root.geometry("550x650")

# Main Frame
main = tk.Frame(root, padx=15, pady=15)
main.pack(fill="both", expand=True)

main.columnconfigure(1, weight=1)

# Student Information
student = tk.LabelFrame(main, text="Student Information")
student.grid(row=0, column=0, columnspan=2,
             sticky="ew", pady=8)

tk.Label(student, text="Name").grid(row=0, column=0)

name = tk.Entry(student)
name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(student, text="Department").grid(row=1, column=0)

department = ttk.Combobox(
    student,
    values=["CS", "IT", "IS"],
    state="readonly"
)
department.grid(row=1, column=1, padx=10, pady=5)

# Study Mode
study = tk.LabelFrame(main, text="Study Mode")
study.grid(row=1, column=0, sticky="ew", pady=8)

mode = tk.StringVar(value="On Campus")

for i, item in enumerate(
    ["On Campus", "Online", "Hybrid"]
):
    tk.Radiobutton(
        study, text=item,
        variable=mode, value=item
    ).grid(row=i, column=0, sticky="w")

# Preferences
prefs = tk.LabelFrame(main, text="Preferences")
prefs.grid(row=1, column=1, sticky="ew", pady=8)

email = tk.BooleanVar()
sms = tk.BooleanVar()
notifications = tk.BooleanVar()

tk.Checkbutton(prefs, text="Email",
               variable=email).pack(anchor="w")

tk.Checkbutton(prefs, text="SMS",
               variable=sms).pack(anchor="w")

tk.Checkbutton(prefs, text="Notifications",
               variable=notifications).pack(anchor="w")

# Experience
tk.Label(main, text="Experience Level").grid(
    row=2, column=0, sticky="w"
)

experience = tk.Scale(
    main, from_=1, to=10,
    orient="horizontal"
)
experience.grid(row=2, column=1, sticky="ew")

# Skills
skills_frame = tk.LabelFrame(main, text="Skills")
skills_frame.grid(row=3, column=0,
                  columnspan=2, sticky="ew", pady=8)

scroll = tk.Scrollbar(skills_frame)
scroll.pack(side="right", fill="y")

skills = tk.Listbox(
    skills_frame,
    height=5,
    selectmode=tk.EXTENDED,
    yscrollcommand=scroll.set
)
skills.pack(fill="x")

scroll.config(command=skills.yview)

for item in ["Python", "Java", "C++",
             "HTML", "CSS", "SQL"]:
    skills.insert(tk.END, item)

# Summary
summary = tk.LabelFrame(main, text="Summary")
summary.grid(row=4, column=0,
             columnspan=2, sticky="ew", pady=8)

output = tk.Label(summary, text="No Data",
                  justify="left")
output.pack(anchor="w")

def save():
    if not name.get().strip() or not department.get():
        messagebox.showerror(
            "Error", "Name and Department are required"
        )
        return

    selected = [
        skills.get(i)
        for i in skills.curselection()
    ]

    if not selected:
        messagebox.showerror(
            "Error", "Select at least one skill"
        )
        return

    data = (
        f"Name: {name.get()}\n"
        f"Department: {department.get()}\n"
        f"Study Mode: {mode.get()}\n"
        f"Email: {email.get()}\n"
        f"SMS: {sms.get()}\n"
        f"Notifications: {notifications.get()}\n"
        f"Experience: {experience.get()}\n"
        f"Skills: {', '.join(selected)}"
    )

    output.config(text=data)

def reset():
    name.delete(0, tk.END)
    department.set("")
    mode.set("On Campus")

    email.set(False)
    sms.set(False)
    notifications.set(False)

    experience.set(1)
    skills.selection_clear(0, tk.END)

    output.config(text="No Data")

def exit_app():
    if messagebox.askyesno("Exit", "Are you sure?"):
        root.destroy()

buttons = tk.Frame(main)
buttons.grid(row=5, column=0,
             columnspan=2, pady=10)

tk.Button(buttons, text="Save",
          command=save).pack(side="left", padx=5)

tk.Button(buttons, text="Reset",
          command=reset).pack(side="left", padx=5)

tk.Button(buttons, text="Exit",
          command=exit_app).pack(side="left", padx=5)

root.mainloop()
