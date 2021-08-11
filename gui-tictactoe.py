from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic-Tac-Toe-blah-blah')
# root.geometry("480x480")


def btn_click(btn):
    pass


# we need 9 buttons for the tictactoe grid
b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: btn_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: btn_click(b2))
b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: btn_click(b3))

b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: btn_click(b4))
b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: btn_click(b5))
b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: btn_click(b6))

b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: btn_click(b7))
b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: btn_click(b8))
b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: btn_click(b9))

# Grid buttons to screen
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

root.mainloop()