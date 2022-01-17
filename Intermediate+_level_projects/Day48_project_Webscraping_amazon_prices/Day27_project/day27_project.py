import tkinter

def button_func():
    if input.get():
        input_text = float(input.get())
        answer = round(input_text * 1.609344, 2)
        label_list[1].config(text = answer) 


window = tkinter.Tk()
window.title("Miles to KM Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

text_first_row = ['', '', 'Miles']
for i in range(3):
    if i == 1:
        input = tkinter.Entry(width=7)
        input.grid(column=i, row=0)

    else:    
        label = tkinter.Label(text=text_first_row[i])
        label.grid(column=i, row=0)

text_second_row = ['is equal to', '0', 'Km']
label_list = []
for j in range(3):
    label = tkinter.Label(text=text_second_row[j])
    label_list.append(label)
    label_list[j].grid(column=j, row=1)

button = tkinter.Button(text="Calculate", command=button_func)
button.grid(column=1, row=2)


window.mainloop()