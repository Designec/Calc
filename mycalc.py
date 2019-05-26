from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title('Calculator')


def clear():
    entry.delete(0, END)


def eq(eqkey):
    if eqkey == '=':
        allsimbols = '-+01234567890.*/='
        if entry.get()[0] not in allsimbols:
            messagebox.showerror('Ошибка!', 'Вы ввели не число!')
        try:
            result = eval(entry.get())
            entry.delete(0, END)
            entry.insert(END, result)
        except:
            messagebox.showerror("Ошибка!", 'Проверь правильность данных')


def calc(key):
    if key == '+/-':
        if '=' in entry.get():
            entry.delete(0, END)
        try:
            if entry.get()[0] == '-':
                entry.delete(0)
            else:
                entry.insert(0, '-')
        except IndexError:
            pass

    else:
        if '=' in entry.get():
            entry.delete(0, END)
        entry.insert(END, key)


entry = Entry(font='Arial 20', justify=RIGHT)
entry.grid(row=0, columnspan=4, sticky=W + E)

btnList = [
    '1', '2', '3', '/',
    '4', '5', '6', '*',
    '7', '8', '9', '-',
    '.', '0', '+/-', '+',
    '=', 'C'
]

r = 2
c = 0


for i in btnList:
    if i == '=':
        ttk.Button(window, text=i, command=lambda x=i: eq(x)).grid(column=0, columnspan=4, row=8, ipadx='10',
                                                                   ipady='10', sticky=W + E)
    elif i == 'C':
        ttk.Button(window, text=i, command=clear).grid(column=0, columnspan=4, row=1, ipadx='10',
                                                       ipady='10', sticky=W + E)
    else:
        ttk.Button(window, text=i, command=lambda x=i: calc(x)).grid(row=r, column=c, ipadx='10', ipady='10')
    c += 1
    if c > 3:
        c = 0
        r += 1

window.mainloop()
