# 원리합계 프로그램
m = int(input("예금 금액(원): ")) #금액
rate = float(input("예금 이율(%): ")) #이율
d = int(input("예금 기간(년): ")) #기간
print("#" * 20)
result = m + (m * rate * 0.01 * d)
print(f'{m}을 {rate}% 이율로 {d}년간 예치 후 원리합계는 {result:.0f}원')