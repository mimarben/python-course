import tkinter as tk

window = tk.Tk()

window.title("My first GUI program")
window.minsize(width=800, height=400)
my_label = tk.Label(text="Hello World!!", font=("Arial", 20, "bold"))
my_label.pack(expand=True)










window.mainloop()
