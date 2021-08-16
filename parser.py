from bs4 import BeautifulSoup
import requests
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django

django.setup()

from crawler.models import AiData, ComData


def extract_data(data):
    try:
        data.find("td", {"class": "no"}).find("span")
        title = data.find("td", {"class": "title"}).get_text().strip()
        link = data.find("td", {"class": "title"}).find("a")["href"]
        link = f"https://builder.hufs.ac.kr/user/{link}"
        author = data.find_all("td")[2].get_text().strip()
        date = data.find_all("td")[3].get_text().strip()
        data_dic = {
            "title": title,
            "link": link,
            "author": author,
            "date": date,
        }
    except:
        pass
    return data_dic


def extract_datas(url, last_page):
    datas = []
    for page in range(last_page):
        print(f"Scrapping: {page+1} / {last_page}")
        url = f"{url}&page={page+1}&command=list"
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "html.parser")
        datas_list = (
            soup.find("table", {"summary": "게시판리스트"}).find("tbody").find_all("tr")
        )
        for data in datas_list:
            data_dic = extract_data(data)
            datas.append(data_dic)
    return datas


def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "paging"}).find_all("a")
    last_page = len(pages)
    return last_page


def get_datas(id, board_id):
    url = f"http://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId={id}&dum=dum&boardId={board_id}"
    last_page = get_last_page(url)
    datas = extract_datas(url, last_page)
    return datas


AI_ID = "ai"
AI_BOARD_ID = 150797968
COM_ID = "ces"
COM_BOARD_ID = 43626718


if __name__ == "__main__":
    ai_data_dict = get_datas(AI_ID, AI_BOARD_ID)
    for data in ai_data_dict:
        AiData(
            title=data["title"],
            author=data["author"],
            date=data["date"],
            link=data["link"],
        ).save()
    com_data_dict = get_datas(COM_ID, COM_BOARD_ID)
    for data in com_data_dict:
        ComData(
            title=data["title"],
            author=data["author"],
            date=data["date"],
            link=data["link"],
        ).save()
