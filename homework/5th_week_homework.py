import tkinter as tk


def save():
    info = (
        f"Name: {name.get()}\n"
        f"ID: {sid.get()}\n"
        f"Email: {email.get()}\n"
        f"Department: {department.get()}\n"
        f"Semester: {semester.get()}\n"
        f"Phone: {phone.get()}"
    )

    if not all([
        name.get().strip(),
        sid.get().strip(),
        email.get().strip(),
        department.get().strip(),
        semester.get().strip(),
        phone.get().strip()
    ]):
        status.config(text="Please fill all fields")
        return

    status.config(text=info)


def clear():
    for entry in entries:
        entry.delete(0, tk.END)

    status.config(text="Form cleared")


root = tk.Tk()
root.title("Personal Information Form")
root.geometry("550x500")

header = tk.Frame(root, bg="lightblue")
header.pack(fill="x")

tk.Label(
    header,
    text="Personal Information",
    font=("Arial", 20, "bold"),
    bg="lightblue"
).pack(pady=15)

form = tk.Frame(root, padx=20, pady=20)
form.pack(fill="both", expand=True)

form.columnconfigure(1, weight=1)

fields = [
    "Full Name",
    "Student ID",
    "Email",
    "Department",
    "Semester",
    "Phone"
]

entries = []

for row, field in enumerate(fields):
    tk.Label(form, text=field).grid(
        row=row, column=0, sticky="w", pady=8
    )

    entry = tk.Entry(form)
    entry.grid(
        row=row, column=1, sticky="ew", padx=10, pady=8
    )

    entries.append(entry)

name, sid, email, department, semester, phone = entries

actions = tk.Frame(root)
actions.pack(pady=10)

tk.Button(actions, text="Save", command=save).pack(side="left", padx=5)
tk.Button(actions, text="Clear", command=clear).pack(side="left", padx=5)
tk.Button(actions, text="Exit", command=root.destroy).pack(side="left", padx=5)

status = tk.Label(root, text="Ready", justify="left")
status.pack(pady=10)

root.mainloop()