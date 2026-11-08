import tkinter as tk
import random

def generate():
    number = number_entry.get()

    if len(number) != 3 or not number.isdecimal():
        return

    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    block = ''
    for i in range(5):
        block += random.choice(symbols)

    shift = int(number[0])
    short_block = block[:-1]

    new_block = ''
    for char in short_block:
        position = symbols.index(char)
        new_position = (position + shift) % len(symbols)
        new_block += symbols[new_position]

    key = block + '-' + new_block


    shift = int(number[1])
    short_block = new_block[:-1]

    new_block = ''
    for char in short_block:
        position = symbols.index(char)
        new_position = (position - shift) % len(symbols)
        new_block += symbols[new_position]

    key += '-' + new_block

    shift = int(number[2])
    short_block = new_block[:-1]

    new_block = ''
    for char in short_block:
        position = symbols.index(char)
        new_position = (position + shift) % len(symbols)
        new_block += symbols[new_position]

    key += '-' + new_block

    key_entry.delete(0, 'end')
    key_entry.insert(0, key)


window = tk.Tk()
window.title('My app')
window.geometry('800x450')
window.resizable(0, 0)

background = tk.PhotoImage(file='background.png')

background_label = tk.Label(window, image=background)
background_label.place(relwidth=1, relheight=1)

label1 = tk.Label(
    window,
    text='Введите трёхзначное число',
    font=('Arial', 14),
    bg='darkgreen',
    fg='white'
)
label1.pack(pady=(140, 10))

number_entry = tk.Entry(
    window,
    font=('Arial', 16),
    justify='center',
    width=12,
    bg='white',
    fg='black'
)
number_entry.pack(pady=5)


button = tk.Button(
    window,
    text='Сгенерировать',
    command=generate,
    font=('Arial', 12),
    bg='green',
    fg='white'
)
button.pack(pady=12)

key_entry = tk.Entry(
    window,
    font=('Consolas', 16),
    justify='center',
    width=22,
    bg='white',
    fg='black'
)
key_entry.pack(pady=5)


window.mainloop()
