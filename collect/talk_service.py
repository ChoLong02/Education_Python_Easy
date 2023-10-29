import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def set_driver():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=options)
    return driver


def get_info(url: str):
    doc = requests.get(url)
    doc = BeautifulSoup(doc.text, "html.parser")

    title = doc.select("h3.tit_view")[0].get_text()
    content_list = doc.select("div.bbs_view > p")

    main_text = ""
    for content in content_list:
        main_text += content.get_text().strip()

    reg_date = doc.select("span.tit_cat")[1].get_text()
    return title, main_text, reg_date
