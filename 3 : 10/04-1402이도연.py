print("#" * 20)
print("  BMI 계산 프로그램")
print("#" * 20)
height = float(input("키(cm): ")) # 키
weight = float(input("몸무게(kg): ")) # 몸무게
print("#" * 20)
result = weight / (height / 100) ** 2 # BMI
print(f'당신의 BMI 지수는 {result:.1f} 입니다.')