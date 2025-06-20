# 클래스 정의
class MemberInfo:
    def __init__(self, idx, passwd, name):#self자리엔 객체이름 들어감
        self.idx = idx
        self.passwd = passwd
        self.name = name

    def getMember(self):
        return f'{self.idx}, {self.passwd}, {self.name}'
    
# 객체생성과 사용
my_member = MemberInfo('king', '123456', '홍길동')
print(my_member.getMember())