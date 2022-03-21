#함수를 '1개만' 작성해 공백으로 구분되어 입력받은 두 정수의 합, 차, 곱, 몫, 나머지를 한 줄씩 순서대로 출력하세요

A, B = map(int, input().split())


def cal(a, b):
    # list 
    num1 = a + b
    num2 = a - b
    num3 = a * b
    num4 = a // b
    num5 = a % b



    list = [num1, num2, num3, num4, num5]

    return list
    # return i for _ in list

# string = aTob(a)

for i in cal(A, B):
    print(i)