import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
label = tkinter.Label(text="TEST", font= ("Arial", 20, "bold"))
label.pack()



def button_func():
    input_text = input.get()
    label.config(text = input_text) 

button = tkinter.Button(text="Click Me", command=button_func)
button.pack()


input = tkinter.Entry(width=50)
input.pack()



window.mainloop()