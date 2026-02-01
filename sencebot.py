# Requirements:
# pip install psutil

import tkinter as tk
import psutil
import time
import platform
from datetime import datetime

BG = "#f7f8f8"
ACCENT = "#00eeff"
TEXT = "black"

# ---------------- MAIN APP ----------------
root = tk.Tk()
root.title("SenseBot")
root.geometry("720x450")
root.config(bg=BG)

# ---------------- HEADER ----------------
tk.Label(
    root,
    text="SenseBot 🤖",
    fg=ACCENT,
    bg=BG,
    font=("Arial", 22, "bold")
).pack(pady=10)

# ---------------- DASHBOARD ----------------
dash = tk.Frame(root, bg=BG)
dash.pack(fill="x", padx=20)

cpu_label = tk.Label(dash, fg=TEXT, bg=BG, font=("Arial", 12))
cpu_label.pack(anchor="w")

ram_label = tk.Label(dash, fg=TEXT, bg=BG, font=("Arial", 12))
ram_label.pack(anchor="w")

sys_label = tk.Label(dash, fg="gray", bg=BG, font=("Arial", 10))
sys_label.pack(anchor="w", pady=4)

# ---------------- ASSISTANT AREA ----------------
assistant_frame = tk.Frame(root, bg=BG)
assistant_frame.pack(fill="both", expand=True, padx=20, pady=10)

output = tk.Text(
    assistant_frame,
    height=8,
    bg="black",
    fg=ACCENT,
    insertbackground=ACCENT,
    font=("Consolas", 11)
)
output.pack(fill="both", expand=True)

entry = tk.Entry(
    assistant_frame,
    font=("Arial", 12),
    bg="black",
    fg=TEXT,
    insertbackground=TEXT
)
entry.pack(fill="x", pady=6)

# ---------------- SYSTEM UPDATE ----------------
def update_system():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent

    cpu_label.config(text=f"CPU Usage: {cpu}%")
    ram_label.config(text=f"RAM Usage: {ram}%")

    root.after(1000, update_system)

# ---------------- ASSISTANT LOGIC ----------------
def respond(event=None):
    cmd = entry.get().lower()
    entry.delete(0, "end")

    output.insert("end", f"> {cmd}\n")

    if "time" in cmd:
        reply = datetime.now().strftime("%H:%M:%S")
    elif "date" in cmd:
        reply = datetime.now().strftime("%d %B %Y")
    elif "system" in cmd:
        reply = platform.system()
    elif "cpu" in cmd:
        reply = f"CPU Usage: {psutil.cpu_percent()}%"
    elif "ram" in cmd:
        reply = f"RAM Usage: {psutil.virtual_memory().percent}%"
    elif cmd in ["clear", "cls"]:
        output.delete("1.0", "end")
        return
    else:
        reply = "Command not recognized"

    output.insert("end", reply + "\n\n")
    output.see("end")

entry.bind("<Return>", respond)

# ---------------- SYSTEM INFO ----------------
sys_label.config(
    text=f"{platform.system()} | {platform.processor()}"
)

update_system()
root.mainloop()