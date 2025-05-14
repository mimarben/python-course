import tkinter as tk
import time

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")

        self.sample_text = "The quick brown fox jumps over the lazy dog."

        self.label = tk.Label(root, text="Type the following text as fast and accurately as you can:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.sample_label = tk.Label(root, text=self.sample_text, font=("Arial", 12), wraplength=580)
        self.sample_label.pack(pady=10)

        self.typing_area = tk.Text(root, height=5, font=("Arial", 12))
        self.typing_area.pack(pady=10)
        self.typing_area.config(state=tk.DISABLED)

        self.start_button = tk.Button(root, text="Start Test", command=self.start_test)
        self.start_button.pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.start_time = None

    def start_test(self):
        self.typing_area.config(state=tk.NORMAL)
        self.typing_area.delete(1.0, tk.END)
        self.typing_area.focus()
        self.result_label.config(text="")
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.root.after(60000, self.end_test)  # Automatically end after 60 seconds

    def end_test(self):
        self.typing_area.config(state=tk.DISABLED)
        end_time = time.time()
        typed_text = self.typing_area.get(1.0, tk.END).strip()
        word_count = len(typed_text.split())
        time_elapsed = end_time - self.start_time
        wpm = word_count / (time_elapsed / 60)
        self.result_label.config(text=f"Your typing speed is {wpm:.2f} words per minute.")
        self.start_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
