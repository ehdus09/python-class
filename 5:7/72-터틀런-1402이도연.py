# t. 안쓰고 편하게 필요한 함수 사용가능
from turtle import * # 기말에 나옴
import random as r #먹이 랜덤 위치 이동

#등장인물 만들기
# 한 개만 쓸 때는 객체를 따로 안만들어도 임의의 객체 한 개가 생성이 되기 때문에 t.이라고 쓰면됨
# tc.없이 그냥 color()쓰면 다른 임의의 거북이 한 개 더 생김
tc = Turtle() # 주인공 거북(흰색)
tc.shape('turtle')
tc.color('white')
tc.up()
tc.speed(0)

# 악당 객체 생성
tv = Turtle() # 악당 거북
tv.shape('turtle')
tv.color('red')
tv.up()
tv.speed(0)
tv.goto(0,200) # 악당 시작 위치

tf = Turtle() # 먹이
tf.shape('circle')
tf.color('green')
tf.up()
tf.goto(0,-200)

# 주인공 움직임 정의(키보드 방향키)
def turn_right():
    tc.setheading(0) #tc만 움직임. 다른건 영향X

def turn_up():
    tc.setheading(90) #seth까지만 써도됨, 절대 각도

def turn_left():
    tc.setheading(180)

def turn_down():
    tc.setheading(270)

#play함수(중요)
def play():
    tc.fd(10) # 주인공 앞으로 이동
    ang = tv.towards(tc.pos()) # 악당 입장. 주인공 위치의 상대 각도, 주인공의 x,y좌표를 받아서
    tv.setheading(ang) # 악당이 주인공 쪽을 바라보게
    tv.fd(9) #악당 앞으로 이동
    
    if tc.distace(tf) < 12: # 주인공과 먹이 거리가 가까우면 (닿았을때) (중심과 중심이 완전히 닿지 않음)
        start_x = r.randint(-230, 230) #약간 안으로 해야지 먹이가 안짤림
        start_y = r.randint(-230, 230)
        tf.goto(start_x, start_y) #먹이를 다른 곳으로 이동
        
    if tc.distance(tv) >= 12: #주인공과 악당 거리가 멀면
        ontimer(play, 100) #0.1초 후 play함수 실행(= 게임 계속 실행) 가까워지면 play함수 실행X->종료, play함수 안 play함수 -> 재귀함수
    

#게임준비
def ready(): #생략된 객체: screen, 메소드가 screen과 관련되어있는 것
    setup(500, 500) # 화면크기
    title("Turtle Run") # 창 제목
    bgcolor("orange") # 배경색
    

def move():
    onkeypress(turn_right, "Right")#right에 괄호 안붙임 괄호붙이면 right누르는거와 상관없이 시작되기 때문
    onkeypress(turn_up, "Up")
    onkeypress(turn_left, "Left")
    onkeypress(turn_down, "Down")
    onkeypress(play, "space") #스페이스 키 눌러서 게임시작 중요(play호출)

#메인
ready() #게임준비
move() # 시작
listen() # 이벤트 감지

exitonclick()