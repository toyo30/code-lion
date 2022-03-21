answer = "3/21은 NEXT 세션하는 날!"

string1 = "2022-03-21은 "
string2 = "next"
string3 = "        세션하는 날!      "

string = string1[6] + '/' + string1[8:12] + string2.upper() + ' ' + string3.strip()

# string1.replace("2022-", "")
if answer == string:
    print("정답입니다!")
    print(f"정답 : {answer}")
    print(f"입력값 : {string}")
else:
    print("틀렸습니다.")
    print(f"정답 : {answer}")
    print(f"입력값 : {string}")