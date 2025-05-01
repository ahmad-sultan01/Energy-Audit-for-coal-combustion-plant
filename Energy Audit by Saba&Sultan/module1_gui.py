
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not file_path:
        return

    try:
        df = pd.read_csv(file_path)
        text.delete("1.0", tk.END)
        text.insert(tk.END, "First 5 Rows:\n")
        text.insert(tk.END, df.head().to_string())
        text.insert(tk.END, "\n\nValidation Report:\n")

        if df.isnull().values.any():
            text.insert(tk.END, "- Warning: Missing values found.\n")
        else:
            text.insert(tk.END, "- No missing values.\n")

        text.insert(tk.END, "\nData Types:\n")
        text.insert(tk.END, df.dtypes.to_string())
        text.insert(tk.END, "\n\nBasic Statistics:\n")
        text.insert(tk.END, df.describe().to_string())

    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Auxiliary Energy Data Validator")

load_button = tk.Button(root, text="Load CSV File", command=load_file)
load_button.pack(pady=10)

text = tk.Text(root, height=30, width=100)
text.pack(padx=10, pady=10)

root.mainloop()
