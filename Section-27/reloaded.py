import hupper
import tkinter as tk

def start_reloader():
    reloader = hupper.start_reloader('reloaded.main')

def main():
    root = tk.Tk()
    root.title("Tkinter App with Live Reloaddd")

    label = tk.Label(root, text="This is a label.")
    label.pack(pady=20)

    button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Label changedasdas!"))
    button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    start_reloader()
    main()