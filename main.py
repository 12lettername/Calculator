from tkinter import *

answer = ""

def equal():
    try:
        global answer
        total = str(eval(answer))

        equation.set(total)
        answer = ""
    except:
        equation.set("error")
        answer = ""

def press(num):
    global answer
    answer += str(num)
    equation.set(answer)

def clear():
    global answer
    answer = ""
    equation.set("")

if __name__ == "__main__":
    win = Tk()

    win.configure(background="black")
    win.title("Calculator")
    win.geometry("440x230")

    equation = StringVar()

    expressionBox = Entry(win, textvariable=equation)

    expressionBox.grid_configure(columnspan=10,ipadx=180)

    button1 = Button(win, text=' 1 ', fg='white', bg='gray',
                     command=lambda: press(1), height=2, width=14)
    button1.grid(row=2, column=0)

    button2 = Button(win, text=' 2 ', fg='white', bg='gray',
                     command=lambda: press(2), height=2, width=14)
    button2.grid(row=2, column=1)

    button3 = Button(win, text=' 3 ', fg='white', bg='gray',
                     command=lambda: press(3), height=2, width=14)
    button3.grid(row=2, column=2)

    button4 = Button(win, text=' 4 ', fg='white', bg='gray',
                     command=lambda: press(4), height=2, width=14)
    button4.grid(row=3, column=0)

    button5 = Button(win, text=' 5 ', fg='white', bg='gray',
                     command=lambda: press(5), height=2, width=14)
    button5.grid(row=3, column=1)

    button6 = Button(win, text=' 6 ', fg='white', bg='gray',
                     command=lambda: press(6), height=2, width=14)
    button6.grid(row=3, column=2)

    button7 = Button(win, text=' 7 ', fg='white', bg='gray',
                     command=lambda: press(7), height=2, width=14)
    button7.grid(row=4, column=0)

    button8 = Button(win, text=' 8 ', fg='white', bg='gray',
                     command=lambda: press(8), height=2, width=14)
    button8.grid(row=4, column=1)

    button9 = Button(win, text=' 9 ', fg='white', bg='gray',
                     command=lambda: press(9), height=2, width=14)
    button9.grid(row=4, column=2)

    button0 = Button(win, text=' 0 ', fg='white', bg='gray',
                     command=lambda: press(0), height=2, width=14)
    button0.grid(row=5, column=0)

    plus = Button(win, text=' + ', fg='white', bg='gray',
                  command=lambda: press("+"), height=2, width=14)
    plus.grid(row=2, column=3)

    minus = Button(win, text=' - ', fg='white', bg='gray',
                   command=lambda: press("-"), height=2, width=14)
    minus.grid(row=3, column=3)

    multiply = Button(win, text=' * ', fg='white', bg='gray',
                      command=lambda: press("*"), height=2, width=14)
    multiply.grid(row=4, column=3)

    divide = Button(win, text=' / ', fg='white', bg='gray',
                    command=lambda: press("/"), height=2, width=14)
    divide.grid(row=5, column=3)

    equal = Button(win, text=' = ', fg='white', bg='gray',
                   command=equal, height=2, width=14)
    equal.grid(row=5, column=2)

    clear = Button(win, text='Clear', fg='white', bg='gray',
                   command=clear, height=2, width=14)
    clear.grid(row=5, column=1)

    Decimal = Button(win, text='.', fg='white', bg='gray',
                     command=lambda: press('.'), height=2, width=14)
    Decimal.grid(row=6, column=0)
    # start the GUI
    win.mainloop()