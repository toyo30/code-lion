import requests
from bs4 import BeautifulSoup

# 우리가 정보를 얻고 싶어하는 URL
EGG_URL = f"https://search.shopping.naver.com/search/all?pagingIndex=2&pagingSize=80&query=반숙란"
#f는 문자열 포메팅을 의미함. 

# get 요청을 통해 해당 페이지 정보를 저장
egg_html = requests.get(EGG_URL)

# 요청을 보냄 


# bs4 라이브러리를 통해 불러온 html을 우리가 원하는 형태로 파싱
egg_soup = BeautifulSoup(egg_html.text, "html.parser")



egg_list_box = egg_soup.find("ul", {"class":"list_basis"})
egg_list = egg_list_box.find_all("li", {"class":"basicList_item__2XT81"})
result = []



for egg in egg_list:
    title = egg.find("div", {"class":"basicList_title__3P9Q7"}).find("a").string
    price = egg.find("div", {"class":"basicList_price_area__1UXXR"}).find("span").text
    detail_lists = egg.find("div", {"class":"basicList_detail_box__3ta3h"}).find_all("a")


    detail = []
    for detail_list in detail_lists:
        detail.append(detail_list.text)

    egg_info = {
        'title': title,
        'price': price,
        'detail': detail
    }

    result.append(egg_info)


# print(len(egg_list))
print(result)




# print(len(egg_soup))






# 크롤링되는지 안 되는지 확인하기 

# User-agent: * 
# Disallow: / 
# Allow: /&

# 메인 페이지만 크롤링이 가능하다. 

#셀래늄을 훨씬 더 많이 사용한다. 