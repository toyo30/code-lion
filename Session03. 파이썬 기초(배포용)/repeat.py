#1. for문을 활용해서 1부터 10까지의 숫자 중 3의 배수는 제외하고 출력해주세요(힌트:continue)

for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)



#2. while 문을 사용하여 아래와 같이 별을 표시하는 프로그램을 작성해주세요
# *
# **
# ***
# ****
# *****


count = 1
while count < 6:
    print('*' * count)
    # print('\n')
    count += 1


#3. 입력받은 줄 수 만큼 별을 오른쪽 정렬로 표시하는 프로그램을 작성해주세요
# 예:
#     *
#    **
#   ***
#  ****

inp = int(input("줄 수를 입력해주세요"))

blank = ' '
star = '*'
for i in range(1, inp + 1):
    print(blank * (inp - i), end='')
    print(star * i)

# line = int(input())




import sys 

point = int(sys.stdin.readline())


# point = int(sys.stdin.readline().rstrip())
#enter가 쳐지게 됨. 

#rjust() 정렬해주기 