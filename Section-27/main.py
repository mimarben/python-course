import tkinter as tk
import hupper
def button_clicked():
    my_label.config(text=input.get())

window = tk.Tk()    
window.title("My first GUI program")
window.minsize(width=800, height=400)
window.geometry("800x400+4800+200")
my_label = tk.Label(text="Hello World!!!!!", font=("Arial", 20, "bold"))
my_label.pack(expand=True)
button= tk.Button(text="Start reloader", command=button_clicked);
button.pack()


input =tk.Entry(width=50)
input.pack(pady=10)



window.mainloop()



