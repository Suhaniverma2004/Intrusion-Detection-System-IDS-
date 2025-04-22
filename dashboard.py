
import tkinter as tk
from tkinter import messagebox, scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from threat_db import load_threats
from log_parser import parse_logs
import os

class IDS_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Intrusion Detection System Dashboard")
        self.root.geometry("900x600")
        self.root.configure(bg="#1e1e2f")

        self.running = True

        self.log_display = scrolledtext.ScrolledText(root, width=100, height=20, bg="#2e2e3e", fg="white")
        self.log_display.pack(pady=10)

        self.canvas_frame = tk.Frame(root, bg="#1e1e2f")
        self.canvas_frame.pack()

        self.threats, self.severities = load_threats()
        self.plot_threats({})

        control_frame = tk.Frame(root, bg="#1e1e2f")
        control_frame.pack(pady=10)

        tk.Button(control_frame, text="Refresh Logs", command=self.update_logs, bg="#6a5acd", fg="white").pack(side=tk.LEFT, padx=10)
        tk.Button(control_frame, text="Clear Logs", command=self.clear_logs, bg="#ff6347", fg="white").pack(side=tk.LEFT, padx=10)
        tk.Button(control_frame, text="Pause/Resume", command=self.toggle_updates, bg="#3cb371", fg="white").pack(side=tk.LEFT, padx=10)

        self.update_logs()

    def plot_threats(self, data):
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(6, 3), dpi=100)
        ax.bar(data.keys(), data.values(), color="orange")
        ax.set_title("Threat Frequency")
        ax.set_ylabel("Count")
        ax.set_xlabel("Threat Type")
        fig.tight_layout()

        chart = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        chart.draw()
        chart.get_tk_widget().pack()

    def update_logs(self):
        if not self.running:
            return

        if os.path.exists("logs.txt"):
            with open("logs.txt", "r") as f:
                lines = f.readlines()
                self.log_display.delete(1.0, tk.END)
                for line in lines:
                    self.log_display.insert(tk.END, line)

        counts = parse_logs("logs.txt", self.threats)
        self.plot_threats(counts)

        if counts:
            for threat, count in counts.items():
                if count > 0:
                    messagebox.showinfo("Alert", f"Threat detected: {threat} x{count}")

        self.root.after(5000, self.update_logs)

    def clear_logs(self):
        open("logs.txt", "w").close()
        self.update_logs()

    def toggle_updates(self):
        self.running = not self.running
        if self.running:
            self.update_logs()

if __name__ == "__main__":
    root = tk.Tk()
    app = IDS_GUI(root)
    root.mainloop()
