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

# print(egg_soup)
# 전체 파일 출력


# egg_list_box = egg_soup.find("div", {"class":"basicList_title__3P9Q7"})
# # print(egg_list_box)
# egg_list = egg_list_box.find_all("a", {"class":"basicList_link__1MaTN"})



#find랑 find_all 의 차이는? 




#------------ 데이터에 접근하기 -------------------------



egg_list_box = egg_soup.find("ul", {"class":"list_basis"})
#여러 가지 li값을 가져와야 하기 때문에 필요하다. 
# class이름  basicList_item__2XT81 ad
#ad를 지워야 한다. 광고 상품말고도 다 뽑아야 하니까. 
egg_list = egg_list_box.find_all("li", {"class":"basicList_item__2XT81"})
title = egg_list[0].find("div", {"class":"basicList_title__3P9Q7"}).find("a").string
price = egg_list[0].find("div", {"class":"basicList_price_area__1UXXR"}).find("span").string
detail_lists = egg_list[0].find("div", {"class":"basicList_detail_box__3ta3h"}).find_all("a")



# title = egg_list[0].find("div", {"class":"basicList_title__3P9Q7"}).find("a").string일 때, 
# type(title)  출력 후 class를 거쳐서 정제됨 <class 'bs4.element.NavigableString'>
# 태그의 하위 문자열을 객체화하여 출력함. 
# 문자열이 없으면 None이 뜸.

# title = egg_list[0].find("div", {"class":"basicList_title__3P9Q7"}).find("a").text일 때, 
# type(title)  출력 후 class를 거쳐서 정제됨 <class 'str'>



#------------ 데이터를 저장하기 -------------------------

# print(type(detail_lists))

detail = []


for detail_list in detail_lists:
    detail.append(detail_list.text)



result = {
    'title': title,
    'price': price,
    'detail': detail
}



print(result)




# print(len(egg_soup))






# 크롤링되는지 안 되는지 확인하기 

# User-agent: * 
# Disallow: / 
# Allow: /&

# 메인 페이지만 크롤링이 가능하다. 

#셀래늄을 훨씬 더 많이 사용한다. 