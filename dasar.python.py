import tkinter as tk

def say_hello_world():
    label.config(text="Hello World 1")
    
window = tk.Tk()
window.title("Hello World")

label = tk.Label(window, text="Hello World")
label.pack(pady=10)

button = tk.Button(window, text="Click Me", command=say_hello_world)
button.pack(pady=10)

window.mainloop()