import tkinter as tk
from tkinter import messagebox
import threading
import time

INACTIVITY_LIMIT = 5  # seconds

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dangerous Writing App")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        self.text = tk.Text(root, wrap="word", font=("Helvetica", 16), bg="black", fg="white", insertbackground="white")
        self.text.pack(expand=True, fill="both", padx=20, pady=20)

        self.start_button = tk.Button(root, text="Start Writing", command=self.start_session, font=("Helvetica", 14))
        self.start_button.pack(pady=10)

        self.inactivity_timer = None
        self.last_keypress_time = None
        self.session_active = False

        self.text.bind("<Key>", self.on_keypress)

    def start_session(self):
        self.text.delete("1.0", tk.END)
        self.session_active = True
        self.start_button.config(state="disabled")
        self.last_keypress_time = time.time()
        self.monitor_inactivity()

    def on_keypress(self, event):
        if self.session_active:
            self.last_keypress_time = time.time()

    def monitor_inactivity(self):
        def check_inactivity():
            while self.session_active:
                elapsed = time.time() - self.last_keypress_time
                if elapsed >= INACTIVITY_LIMIT:
                    self.session_active = False
                    self.clear_text()
                    break
                time.sleep(0.5)
        threading.Thread(target=check_inactivity, daemon=True).start()

    def clear_text(self):
        self.text.delete("1.0", tk.END)
        self.start_button.config(state="normal")
        messagebox.showwarning("Time's up!", "You stopped typing! Your work has been erased.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()
