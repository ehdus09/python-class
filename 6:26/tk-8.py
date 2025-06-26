from tkinter import *
def changeLabel():
    lbl["text"] = "첫 번째 버튼 클릭"

def changeButton():
    button2["text"] = "두 번째 버튼 클릭"


window = Tk()
lbl = Label(window, text="결과 출력 레이블.")
button1 = Button(window, text="One", command=changeLabel)
button2 = Button(window, text="Two", command=changeButton)

lbl.pack()
button1.pack()
button2.pack()

window.mainloop()