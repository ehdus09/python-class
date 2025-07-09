from tkinter import *

root = Tk()
root.title("배치관리자")
root.geometry("300x200")

btn1 = Button(root, text="(0,0)", bg = "green")
btn2 = Button(root, text="(0,1)", bg = "red")
btn3 = Button(root, text="(0,2)", bg = "blue")

btn4 = Button(root, text="(1,0)", bg = "gray")
btn5 = Button(root, text="(1,1)", bg = "yellow")
btn6 = Button(root, text="(1,2)", bg = "pink")

btn7 = Button(root, text="(2,0)", bg = "purple")
btn8 = Button(root, text="(2,1)", bg = "orange")
btn9 = Button(root, text="(2,2)", bg = "cyan")

btn10 = Button(root, text="(3,0)", bg = "royalblue")
btn11 = Button(root, text="(3,1)", bg = "beige")
btn12 = Button(root, text="(3,2)", bg = "brown")

root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=2)
root.rowconfigure(3, weight=3)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=3)

btn1.grid(row=0, column=0, sticky="news")
btn2.grid(row=0, column=1, sticky="news")
btn3.grid(row=0, column=2, sticky="news")
btn4.grid(row=1, column=0, sticky="news")
btn5.grid(row=1, column=1, sticky="news")
btn6.grid(row=1, column=2, sticky="news")
btn7.grid(row=2, column=0, sticky="news")
btn8.grid(row=2, column=1, sticky="news")
btn9.grid(row=2, column=2, sticky="news")
btn10.grid(row=3, column=0, sticky="news")
btn11.grid(row=3, column=1, sticky="news")
btn12.grid(row=3, column=2, sticky="news")

root.mainloop()
