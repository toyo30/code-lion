from tkinter.font import names


class Calculator:
    # 여기에 코드를 작성해보세요!
    # 클래스 명은 항상 대문자로 작성을 해보자. 
   
   #__init__
    #생성자 함수 멤버 변수를 정의하는 것이다. 
    #이것을 소유자의 기초적인 정보. 

    # 기본 정보를 저장함으로써, 제일 먼저 접근하게 되는 함수. 

    #self 함수 내에서는 객체를 가르치는 말이 없다. self로 가르치게 된다. 
    

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.result = 0


    def add(self, num):
        self.result += num
        return self.result
    def sub(self, num):
        self.result -= num
        return self.result
    def mul(self, num):
        self.result *= num
        return self.result
    def div(self, num):
        if (num == 0) :
            print("0으로 나눌 수 없습니다.")
            return None

        self.result /= num
        return self.result





#calculatoer1은 Calculator의 인스턴스, 혹은 객체 


calculator1 = Calculator("박채원", 24)
# calculator2 = Calculator("이영서")
calculator1.add(2)
calculator1.add(10)
calculator1.sub(10)


print(calculator1.result)


# 장고의 db모델을 사용할 때, 클래스가 꼭 사용됨