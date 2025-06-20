# 클래스 정의
class Dog:
    def __init__(self, name, age, kind):
        self.name = name
        self.age = age
        self.kind = kind

    def bark(self):
        print(f'{self.name}가 멍멍 짖어요!')
    
    def sit(self):
        print(f'{self.kind}는 앉기도 잘해요')

# 객체 생성과 사용
my_dog = Dog('망고', 3, '푸들')
my_dog.bark()

your_dog = Dog('당근', 5, '진도')
your_dog.sit()