import requests
from bs4 import BeautifulSoup
from sep_egg import extract_info
import csv

file = open('./Session04/egg.csv', mode="w", newline='')
# mode="w" csv 파일에다가 정보를 입력하고 쓰는 모드
# newline = '' 뛰어쓰기 없이 입력

writer = csv.writer(file)
# 쓰기 모드

writer.writerow(["title", "price", "detail"])

final_result = []

for page in range(1, 11):
    # 우리가 정보를 얻고 싶어하는 URL
    EGG_URL = f"https://search.shopping.naver.com/search/all?pagingIndex={page}&pagingSize=80&query=반숙란"
    #f는 문자열 포메팅을 의미함. 

    # get 요청을 통해 해당 페이지 정보를 저장
    egg_html = requests.get(EGG_URL)

    # 요청을 보냄 


    # bs4 라이브러리를 통해 불러온 html을 우리가 원하는 형태로 파싱
    egg_soup = BeautifulSoup(egg_html.text, "html.parser")
    egg_list_box = egg_soup.find("ul", {"class":"list_basis"})
    egg_list = egg_list_box.find_all("li", {"class":"basicList_item__2XT81"})

    #list를 더하는 것은 리스트 안에 요소가 더해짐 
    final_result += extract_info(egg_list)


for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['price'])
    row.append(result['detail'])
    writer.writerow(row)
print(final_result)


