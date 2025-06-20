class Counter:
    def __init__(self): # 생성자. 초기화
        self.count = 0 # 인스턴트 변수
    
    
    def reset(self, initValue = 0):
        self.count = initValue
    
    def increment(self):
        self.count += 1

    def get(self):
        return self.count

#객체 생성과 사용
a = Counter()
b = Counter()

a.reset()
a.increment()
print(a.get())

b.reset(100)
b.increment()
print(b.get())