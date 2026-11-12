import tkinter as tk


def save_employee():
    if not emp_id.get().strip() or not name.get().strip():
        status.config(text="Employee ID and Name are required")
        return

    if not email.get().strip() or not phone.get().strip():
        status.config(text="Email and Phone are required")
        return

    if not position.get().strip():
        status.config(text="Position is required")
        return

    if not address.get("1.0", "end-1c").strip():
        status.config(text="Address is required")
        return

    employee = {
        "ID": emp_id.get(),
        "Name": name.get(),
        "Email": email.get(),
        "Phone": phone.get(),
        "Position": position.get(),
        "Address": address.get("1.0", "end-1c")
    }

    print(employee)

    status.config(text="Employee Saved Successfully")


def clear_form():
    emp_id.delete(0, tk.END)
    name.delete(0, tk.END)
    email.delete(0, tk.END)
    phone.delete(0, tk.END)
    position.delete(0, tk.END)
    address.delete("1.0", tk.END)

    status.config(text="Form Cleared")


root = tk.Tk()
root.title("Employee Registration System")
root.geometry("700x650")

# Header Frame
header = tk.Frame(root, bg="lightblue")
header.pack(fill="x")

tk.Label(
    header,
    text="Employee Registration",
    font=("Arial", 22, "bold"),
    bg="lightblue"
).pack(pady=15)

# Optional Logo
try:
    logo = tk.PhotoImage(file="logo.png")
    logo_label = tk.Label(header, image=logo, bg="lightblue")
    logo_label.pack()
except tk.TclError:
    logo = None

# Form Frame
form = tk.Frame(root, padx=25, pady=20)
form.pack(fill="both", expand=True)

form.columnconfigure(1, weight=1)

# Employee ID
tk.Label(form, text="Employee ID:").grid(
    row=0, column=0, sticky="w", pady=8
)

emp_id = tk.Entry(form)
emp_id.grid(row=0, column=1, sticky="ew", padx=10)

# Name
tk.Label(form, text="Name:").grid(
    row=1, column=0, sticky="w", pady=8
)

name = tk.Entry(form)
name.grid(row=1, column=1, sticky="ew", padx=10)

# Email
tk.Label(form, text="Email:").grid(
    row=2, column=0, sticky="w", pady=8
)

email = tk.Entry(form)
email.grid(row=2, column=1, sticky="ew", padx=10)

# Phone
tk.Label(form, text="Phone:").grid(
    row=3, column=0, sticky="w", pady=8
)

phone = tk.Entry(form)
phone.grid(row=3, column=1, sticky="ew", padx=10)

# Position
tk.Label(form, text="Position:").grid(
    row=4, column=0, sticky="w", pady=8
)

position = tk.Entry(form)
position.grid(row=4, column=1, sticky="ew", padx=10)

# Address
tk.Label(form, text="Address:").grid(
    row=5, column=0, sticky="nw", pady=8
)

address = tk.Text(form, height=5)
address.grid(row=5, column=1, sticky="ew", padx=10)

# Actions Frame
actions = tk.Frame(root)
actions.pack(pady=15)

tk.Button(
    actions, text="Save",
    command=save_employee
).pack(side="left", padx=10)

tk.Button(
    actions, text="Clear",
    command=clear_form
).pack(side="left", padx=10)

tk.Button(
    actions, text="Exit",
    command=root.destroy
).pack(side="left", padx=10)

# Status Frame
status_frame = tk.Frame(root)
status_frame.pack(fill="x")

status = tk.Label(
    status_frame,
    text="Ready",
    font=("Arial", 12, "bold")
)
status.pack(pady=10)

root.mainloop()