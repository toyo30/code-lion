def extract_info(egg_list):
    result = []

    for egg in egg_list:
        title = egg.find("ul", {"class":"img_list"}).find("a").string
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

    return result
