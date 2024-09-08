import tkinter as tk
import customtkinter
from tkinter import messagebox
import random
import csv
import os

# Predefined department codes
DEPARTMENTS = {
    "Officers":"OF",
    "Administrative Staff":"AS",
    "Department of IT":"IT",
    "Department of AI":"AI",
    "Department of Computer Engineering":"CS",
    "Department of E&C":"EC",
    "Department of Civil":"CV",
    "Department of Physics":"PY",
    "Department of Chemistry":"CH",
    "Department of Mathematics":"MT",
    "Department of English":"EN",
    "Technical Department":"TH"
    # Add more departments here
}

# CSV file to store employee data
CSV_FILE = "employee_codes.csv"

# Function to load existing codes from CSV file
def load_existing_codes():
    if not os.path.exists(CSV_FILE):
        return set()
    
    existing_codes = set()
    with open(CSV_FILE, newline='', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            existing_codes.add(row[2])  # Employee code is the third column
    return existing_codes

# Function to save employee data to CSV
def save_to_csv(initials, department, employee_code):
    # Check if the file exists, create it with a header if not
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Initials", "Department", "Employee Code"])
        writer.writerow([initials, department, employee_code])

# Function to generate a unique employee code
def generate_code():
    initials = initials_entry.get().upper()
    department = department_var.get()

    if not initials or not department:
        messagebox.showerror("Error", "Please enter initials and select department!")
        return

    dept_code = DEPARTMENTS[department]
    random_code = random.randint(100000, 999999)

    existing_codes = load_existing_codes()
    employee_code = f"{initials}-{dept_code}-{random_code}"
    
    # Ensure the generated code is unique
    while employee_code in existing_codes:
        random_code = random.randint(100000, 999999)
        employee_code = f"{initials}-{dept_code}-{random_code}"

    # Save the new employee code to the CSV file
    save_to_csv(initials, department, employee_code)
    
    result_label.config(text=f"Generated Employee Code: {employee_code}")

# Setting up the GUI
root = tk.Tk()
root.title("Employee Code Generator")
root.config(bg="#0d3b66")
root.geometry("700x500")
root.resizable(False,False)
# Frame for user input
frame = tk.Frame(root,bg="#0d3b66",)
frame.place(x=130,y=200)

# Employee initials
tk.Label(frame, text="Enter Employee Initials:",bg="#0d3b66",fg="#ffffff",font=("Calibiri", "15", "bold")).grid(row=0, column=0)
initials_entry = tk.Entry(frame,w=30,bd=0)
initials_entry.grid(row=0, column=1)

# Department selection
tk.Label(frame, text="Select Department:",bg="#0d3b66",fg="#ffffff",font=("Calibiri", "15", "bold")).grid(row=1, column=0)
department_var = tk.StringVar(value="Select Department")
department_menu = tk.OptionMenu(frame, department_var, *DEPARTMENTS.keys())
department_menu.grid(row=1, column=1)

# Generate Button
generate_button = tk.Button(frame, text="Generate Code",bd=0,command=generate_code,width=20,pady=10)
generate_button.grid(row=2, columnspan=2,pady=20)

# Result Label
result_label = tk.Label(frame, text="",bg="#0d3b66",fg="#ffffff",font=("Calibiri", "10", "bold"))
result_label.grid(row=3, columnspan=2, pady=10)

# Start the GUI loop
root.mainloop()
