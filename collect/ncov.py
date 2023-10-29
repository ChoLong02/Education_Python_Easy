# from~import → 외부 모듈 가져오기
# 외부 모듈? 외부 개발자가 만든 코드 집합
#   - Python은 다양한 외부 모듈 존재
#   ex) matplotlib → 그래프 그릴 때 사용하는 외부모듈
#       tensorflow → 인공지능 만들 때 사용하는 외부모듈
#       BeautifulSoup → 웹 크롤링할 때 사용하는 외부모듈

# 외부모듈 사용하는 방법
#  1.외부모듈 다운로드
#  2.from~import로 외부모듈 가져오기
#  3.외부모듈 사용하기 ex) 외부모듈이름.@ 형식으로 사용

# from~import : 일부분 모듈
# import : 전체 모듈
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Selenium 동작원리
#  → selenium만 전용으로 사용하는 웹 브라우저를 통해서 데이터를 수집
#  → 따라서, 전용 웹브라우저 설정 필요 → Chrome, Edge, Firfox 등등

# 1.ChromeDriver 설정
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

# 2.전체 코드 가져오기
url = "https://ncov.kdca.go.kr/tcmBoardView.do?brdId=3&brdGubun=31&dataGubun=&ncvContSeq=7279&contSeq=7279&board_id=312&gubun=BDJ"
driver.get(url)

doc_html = driver.page_source
doc = BeautifulSoup(doc_html, "html.parser")

title = doc.select("div.bv_ttl > h4")[0].get_text()
print(f"제목: {title}")

contents = doc.select("div.bvc_txt > p")

content = ""
for p in contents:
    content += p.get_text()

print(f"본문: {content}")



