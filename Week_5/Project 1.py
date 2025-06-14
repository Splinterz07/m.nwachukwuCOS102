import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Load the CSV file
try:
    df = pd.read_csv("GIG-logistics.csv")
except FileNotFoundError:
    df = pd.DataFrame(columns=["Name", "Department"])
    print("CSV file not found. Please make sure 'GIG-logistics.csv' is in the same folder.")

# GUI App
class EmployeeCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GIG Logistics - Employee Verification")
        self.root.geometry("500x350")
        self.root.resizable(False, False)

        tk.Label(root, text="Employee Name:", font=("Segoe UI", 10)).pack(pady=5)
        self.name_entry = tk.Entry(root, width=40)
        self.name_entry.pack(pady=5)

        tk.Label(root, text="Department:", font=("Segoe UI", 10)).pack(pady=5)
        self.dept_entry = tk.Entry(root, width=40)
        self.dept_entry.pack(pady=5)

        tk.Button(root, text="🔍 Verify Employee", bg="#211C84", fg="white", font=("Segoe UI", 10, "bold"),
                  command=self.verify_employee).pack(pady=10)

        self.result_text = tk.Text(root, height=10, width=60, state="disabled")
        self.result_text.pack(pady=10)

    def verify_employee(self):
        name = self.name_entry.get().strip()
        dept = self.dept_entry.get().strip()

        if not name or not dept:
            messagebox.showwarning("Missing Input", "Please enter both name and department.")
            return

        matches = df[(df["Name"].str.lower() == name.lower()) & (df["Department"].str.lower() == dept.lower())]

        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)

        if not matches.empty:
            self.result_text.insert(tk.END, f"✅ Welcome, {name}!\n\n")
            others = df[(df["Department"].str.lower() == dept.lower()) & 
                        (df["Name"].str.lower() != name.lower())]
            if not others.empty:
                self.result_text.insert(tk.END, f"🧑‍🤝‍🧑 Other members of the {dept} department:\n")
                for other_name in others["Name"]:
                    self.result_text.insert(tk.END, f" - {other_name}\n")
            else:
                self.result_text.insert(tk.END, "You are the only member in this department.")
        else:
            self.result_text.insert(
                tk.END,
                f"Sorry, we couldn’t find anyone named \"{name}\" in the \"{dept}\" department.\n"
                f"Please check the spelling or contact HR for assistance."
            )

        self.result_text.config(state="disabled")


# Launch App
if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeCheckerApp(root)
    root.mainloop()
