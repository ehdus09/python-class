import random

#함수 정의(문자열도 choice 가능)
def genPass():
    chr = 'abcdefghijklmnopqrstuvwxyz0123456789'
    special = '!@#$%^&*'
    length = list(range(8, 16))

    passwd = ""
    for i in range(random.choice(length)):
        passwd += random.choice(chr)
    passwd += random.choice(special)
    passwd = list(passwd)
    random.shuffle(passwd)
    passwd = ''.join(passwd)
    return passwd
    # passwd = random.choices(chr, k=8)
    # return passwd


#main
for i in range(3):
    result = genPass()
    print(f"암호 {i+1}: \033[31m {result} \033[0m")