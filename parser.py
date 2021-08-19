from bs4 import BeautifulSoup
import requests
import urllib
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django

django.setup()

from crawler.models import AiNotice, ComNotice


def extract_data(data):
    try:
        number = data.find("td", {"class": "no"}).find("span").get_text().strip()
        number = int(number)
        title = data.find("td", {"class": "title"}).get_text().strip()
        author = data.find_all("td")[2].get_text().strip()
        link = data.find("td", {"class": "title"}).find("a")["href"]
        link = f"https://builder.hufs.ac.kr/user/{link}"
        date = data.find_all("td")[3].get_text().strip()
        data_dic = {
            "title": title,
            "author": author,
            "number": number,
            "link": link,
            "date": date,
        }
    except:
        return None
    return data_dic


def extract_datas(url, last_page):
    datas = []
    for page in range(last_page):
        print(f"Scrapping: {page+1} / {last_page}")
        link = f"{url}&page={page+1}"
        result = requests.get(link)
        soup = BeautifulSoup(result.text, "html.parser")
        datas_list = (
            soup.find("table", {"summary": "게시판리스트"}).find("tbody").find_all("tr")
        )
        for data in datas_list:
            data_dic = extract_data(data)
            if data_dic != None:
                datas.append(data_dic)
    return datas


def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    href = soup.find("div", {"class": "paging"}).find_all("a")[-1]["href"]
    result = urllib.parse.urlparse(href)
    query = urllib.parse.parse_qs(result.query)
    page = query.get("page")[0]
    return int(page)


def get_datas(id, board_id):
    url = f"https://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId={id}&dum=dum&boardId={board_id}"
    last_page = get_last_page(url)
    datas = extract_datas(url, last_page)
    return datas


AI_ID = "ai"
AI_BOARD_ID = 150797968
COM_ID = "ces"
COM_BOARD_ID = 43626718


if __name__ == "__main__":
    print("AI")
    ai_data_dict = get_datas(AI_ID, AI_BOARD_ID)
    for data in ai_data_dict:
        AiNotice(
            title=data["title"],
            number=data["number"],
            author=data["author"],
            date=data["date"],
            link=data["link"],
        ).save()
    print("COM")
    com_data_dict = get_datas(COM_ID, COM_BOARD_ID)
    for data in com_data_dict:
        ComNotice(
            title=data["title"],
            number=data["number"],
            author=data["author"],
            date=data["date"],
            link=data["link"],
        ).save()
