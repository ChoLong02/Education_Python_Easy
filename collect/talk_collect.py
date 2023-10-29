import requests
from bs4 import BeautifulSoup
from collect.talk_service import get_info, set_driver
from db.TalkDAO import add_talk

count = 0  # 수집 건수 Count

url = "https://news.sarangbang.com/talk/bbs/story"
doc = requests.get(url)
doc = BeautifulSoup(doc.text, "html.parser")

info_list = doc.select("tbody#bbsResult > tr")


for tag in info_list:
    # 게시글 번호 가져오기(공지, 등등 불순물 확인 및 제거)
    tbl_no = tag.select("td")[0].get_text()

    if count == 3:
        exit()
    if tbl_no.isdigit():
        count += 1
        tbl_a = tag.select("td > a")[0]
        url = "https://news.sarangbang.com/" + tbl_a["href"]
        print("=" * 150)
        print(f"{count} → url({url})")
        title, main_text, reg_date = get_info(url)
        print(f"TITLE: {title}")
        print(f"CONTENT: {main_text}")
        print(f"DATE: {reg_date}")

        data = {
            "title": title,
            "content": main_text,
            "date": reg_date
        }
        add_talk(data)
