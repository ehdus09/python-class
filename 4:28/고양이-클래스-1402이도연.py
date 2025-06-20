class Cat: #대문자로 시작
    species = '고양이' #클래스바로 안에 있으면 클래스변수(공용)
    def __init__(self, name, color):
        self.name = name # self는 객체 자기자신을 가르킴
        # 인스턴스의 이름(인스턴스 변수) 공용X