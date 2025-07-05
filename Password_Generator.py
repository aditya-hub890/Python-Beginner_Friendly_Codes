import tkinter as tk
import random
import string

def generate():
    characters = string.ascii_letters + string.digits
    password="".join(random.choice(characters) for __ in range(12))
    result_label.config(state="normal")
    result_label.delete(0,tk.END)
    result_label.insert(0,password)
    result_label.config(state="normal")


win=tk.Tk()
win.title("Password Generator")
win.geometry("300x200")

button=tk.Button(win,text="Click to generate a password",font=("Arial",14),command=generate)
button.pack(pady=(40,10))

result_label=tk.Entry(win,text="",font=("Arial",14))
result_label.config(state="normal")      
result_label.pack(pady=10)

label=tk.Label(win,text="")
label.pack()

win.mainloop()


    

