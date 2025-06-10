import tkinter as tk
from tkinter import messagebox, ttk

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    languages = []
    if python_var.get():
        languages.append("Python")
    if java_var.get():
        languages.append("Java")
    if js_var.get():
        languages.append("JavaScript")
    selected_country = country_combo.get() if country_combo.get() else "None"

    info = f"Name: {name}\nAge: {age}\nGender: {gender}\nLanguages: {', '.join(languages)}\nCountry: {selected_country}"
    messagebox.showinfo("Submitted Info", info)

def clear_form():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set("Not specified")
    python_var.set(False)
    java_var.set(False)
    js_var.set(False)
    country_combo.set('')

root = tk.Tk()
root.title("User Info Form")
root.geometry("420x420")
root.resizable(False, False)

main_frame = ttk.Frame(root, padding="20 15 20 15")
main_frame.grid(row=0, column=0, sticky="NSEW")

# Name
ttk.Label(main_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
name_entry = ttk.Entry(main_frame, width=28)
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

# Age
ttk.Label(main_frame, text="Age:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
age_entry = ttk.Entry(main_frame, width=28)
age_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

# Gender
gender_frame = ttk.LabelFrame(main_frame, text="Gender")
gender_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=10, sticky='ew')
gender_var = tk.StringVar(value="Not specified")
ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").grid(row=0, column=0, padx=5, pady=2)
ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").grid(row=0, column=1, padx=5, pady=2)
ttk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other").grid(row=0, column=2, padx=5, pady=2)

# Languages
lang_frame = ttk.LabelFrame(main_frame, text="Languages Known")
lang_frame.grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky='ew')
python_var = tk.BooleanVar()
java_var = tk.BooleanVar()
js_var = tk.BooleanVar()
ttk.Checkbutton(lang_frame, text="Python", variable=python_var).grid(row=0, column=0, padx=5, pady=2)
ttk.Checkbutton(lang_frame, text="Java", variable=java_var).grid(row=0, column=1, padx=5, pady=2)
ttk.Checkbutton(lang_frame, text="JavaScript", variable=js_var).grid(row=0, column=2, padx=5, pady=2)

# Country
ttk.Label(main_frame, text="Country:").grid(row=4, column=0, padx=5, pady=10, sticky='e')
countries = ["Bangladesh", "India", "USA", "UK", "Canada"]
country_combo = ttk.Combobox(main_frame, values=countries, state="readonly", width=26)
country_combo.grid(row=4, column=1, padx=5, pady=10, sticky='w')

# Buttons
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=5, column=0, columnspan=2, pady=15)
ttk.Button(button_frame, text="Submit", command=submit_form).grid(row=0, column=0, padx=10)
ttk.Button(button_frame, text="Clear", command=clear_form).grid(row=0, column=1, padx=10)

root.mainloop()
