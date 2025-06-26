from tkinter import *
window = Tk()

lbl1 = Label(window, text="레이블 입니다.")
btn1 = Button(window, text = "첫번째 버튼")
btn2 = Button(window, text = "두번째 버튼")

lbl1.pack()
btn1.pack(side=LEFT, pady = 50)
btn2.pack(side=LEFT, padx = 10) #외부 여백 주어 가로로 배치. 안쓰면 0
btn1["text"] = "One"
btn2["text"] = "Two"

window.mainloop