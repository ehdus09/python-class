from tkinter import *
window = Tk() #TK클래스로 루트 윈도 생성
# 위젯을 만들고 배치하는 코드 작성

window.title("ehdus")
window.geometry("640x400+100+100") #창크기, 메인화면 시작 좌표
window.resizable(1, 0) # 가로크기 조절 가능, 세로 크기 조절 불가

label = Label(window, text="레이블입니다.")
label.pack()

window.mainloop() # 윈도 닫을 때까지 이벤트 루프에서 대기

