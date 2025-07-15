import tkinter as tk
from tkinter import ttk
import re

def check_strength(event=None):
    password = entry.get()
    strength = 0

    for label in criteria_labels:
        label.config(foreground="grey")

    if len(password) >= 8:
        criteria_labels[0].config(foreground="green")
        strength += 1
    else:
        criteria_labels[0].config(foreground="red")

    if re.search(r"[A-Z]", password):
        criteria_labels[1].config(foreground="green")
        strength += 1
    else:
        criteria_labels[1].config(foreground="red")

    if re.search(r"[a-z]", password):
        criteria_labels[2].config(foreground="green")
        strength += 1
    else:
        criteria_labels[2].config(foreground="red")

    if re.search(r"[0-9]", password):
        criteria_labels[3].config(foreground="green")
        strength += 1
    else:
        criteria_labels[3].config(foreground="red")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        criteria_labels[4].config(foreground="green")
        strength += 1
    else:
        criteria_labels[4].config(foreground="red")

    if strength <= 2:
        strength_label.config(text="🔴 Weak", foreground="red")
    elif strength == 3 or strength == 4:
        strength_label.config(text="🟠 Medium", foreground="orange")
    elif strength == 5:
        strength_label.config(text="🟢 Strong", foreground="green")


window = tk.Tk()
window.title("Password Complexity Checker")
window.geometry("400x350")
window.resizable(False, False)

title_label = ttk.Label(window, text="🔒 Password Complexity Checker", font=("Arial", 16))
title_label.pack(pady=10)

entry = ttk.Entry(window, show="*", width=30, font=("Arial", 14))
entry.pack(pady=10)
entry.bind("<KeyRelease>", check_strength)

strength_label = ttk.Label(window, text="Start typing...", font=("Arial", 14))
strength_label.pack(pady=5)

criteria_texts = [
    "• At least 8 characters",
    "• Contains uppercase letter",
    "• Contains lowercase letter",
    "• Contains number",
    "• Contains special character (!@#$...)"
]
criteria_labels = []
for text in criteria_texts:
    lbl = ttk.Label(window, text=text, font=("Arial", 12), foreground="grey")
    lbl.pack(anchor="w", padx=30)
    criteria_labels.append(lbl)

window.mainloop()
