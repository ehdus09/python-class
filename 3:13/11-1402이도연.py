# 추가
stu = ['홍길동', '일지매']
print(f'현재 프로그래밍 수강 신청자는 {stu}입니다.')
new = input('추가할 학생 이름: ')
stu.append(new)
print(f'{new} 학생의 신청이 완료되었습니다.')
print(f'현재 이 과목의 최종 신청자는 {stu}입니다.')
# 삭제
out = input("철회할 학생 이름: ")
stu.remove(out)
print(f'{out} 학생의 수강 철회가 완료되었습니다.')
print(f'현재 이 과목의 최종 신청자는 {stu}입니다.')
# 개명
before = input("변경 전 이름: ")
after = input("변경 후 이름: ")
stu[stu.index(before)] = after
print(f'요청하신 대로 {before}을(를) {after}(으)로 변경하였습니다.')
print(f'현재 이 과목의 최종 신청자는 {stu}입니다.')