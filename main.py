import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import importlib.util

# List of python scripts to choose from 
scripts = [
    "update_parent.py",
    "templatePars.py",
    "udpate_close.py",
    "udpate_experience.py",
    "update_build.py",
    "update_collect.py",
    "update_craft.py",
    "update_quest.py",
    "remember_columns.py",
    "update_columns.py",
    "download_excell.py"
]

def check_and_install_module(module_name):
    """Check if a module is installed, and if not, install it."""
    if importlib.util.find_spec(module_name) is None:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])

def run_selected_scripts(selected_scripts):
    python_executable = sys.executable
    for script in selected_scripts:
        try:
            subprocess.run([python_executable, script], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"An error occurred while running {script}:\n{e}")
        except FileNotFoundError:
            messagebox.showerror("Error", f"File not found: {script}")

def on_run():
    selected_scripts = [scripts[i] for i in range(len(scripts)) if var[i].get()]
    if not selected_scripts:
        messagebox.showwarning("Warning", "No scripts selected!")
    else:
        # Checking and installing lxml module if needed
        check_and_install_module("lxml")
        
        run_selected_scripts(selected_scripts)
        messagebox.showinfo("Info", "Selected scripts have been run.")

# Create the main window
root = tk.Tk()
root.title("Select Scripts to Run")

# Create checkbuttons for each script
var = [tk.BooleanVar() for _ in scripts]
for i, script in enumerate(scripts):
    chk = tk.Checkbutton(root, text=script, variable=var[i])
    chk.pack(anchor=tk.W)

# Create the run button
run_button = tk.Button(root, text="Run Selected Scripts", command=on_run)
run_button.pack(pady=10)

# Run the application
root.mainloop()
