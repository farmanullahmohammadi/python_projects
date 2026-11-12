
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Registration")
root.geometry("450x550")

tk.Label(root, text="Student Registration",
         font=("Arial", 18)).pack(pady=10)

entries = {}

for field in ["ID", "Name", "Email", "Department"]:
    tk.Label(root, text=field).pack()
    entry = tk.Entry(root, width=35)
    entry.pack(pady=3)
    entries[field] = entry

tk.Label(root, text="Address / Details").pack()

details = tk.Text(root, width=35, height=5)
details.pack(pady=5)

status = tk.Label(root, text="Ready")
status.pack(pady=10)

def show_message(msg):
    status.config(text=msg)
    root.after(3000, lambda: status.config(text="Ready"))

def save(event=None):
    data = [entries[x].get().strip()
            for x in entries]

    if not all(data):
        show_message("Please fill all fields")
        return

    messagebox.showinfo("Saved", "Student Saved Successfully")
    show_message("Student Saved")

def clear(event=None):
    for entry in entries.values():
        entry.delete(0, tk.END)

    details.delete("1.0", tk.END)
    show_message("Form Cleared")

def exit_app():
    if messagebox.askyesno("Exit", "Are you sure?"):
        root.destroy()

tk.Button(root, text="Save", command=save).pack(pady=5)
tk.Button(root, text="Clear", command=clear).pack(pady=5)
tk.Button(root, text="Exit", command=exit_app).pack(pady=5)

root.bind("<Return>", save)
root.bind("<Escape>", clear)
root.bind("<Control-s>", save)

for entry in entries.values():
    entry.bind("<FocusIn>",
               lambda e: show_message("Field Active"))

    entry.bind("<FocusOut>",
               lambda e: show_message("Field Inactive"))

details.bind("<Button-1>",
             lambda e: show_message("Details Selected"))

root.protocol("WM_DELETE_WINDOW", exit_app)

root.mainloop()
