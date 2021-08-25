from bs4 import BeautifulSoup
import requests
import urllib


def extract_data(data, url):
    try:
        number = data.find("td", {"class": "no"}).find("span").get_text().strip()
        number = int(number)
        title = data.find("td", {"class": "title"}).get_text().strip()
        author = data.find_all("td")[2].get_text().strip()
        href = data.find("td", {"class": "title"}).find("a")["href"]
        specific_id = get_id(href)
        link = f"{url}&page=1&command=view&boardSeq={specific_id}"
        date = data.find_all("td")[3].get_text().strip()
        data_dic = {
            "title": title,
            "author": author,
            "number": number,
            "link": link,
            "date": date,
            "specific_id": specific_id,
        }
    except:
        return None
    return data_dic


def extract_datas(url):
    datas = []
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    print(soup)
    return datas


def get_datas():
    url = f"https://wis.hufs.ac.kr/src08/jsp/lecture/LECTURE2020L.jsp"
    datas = extract_datas(url)
    return datas


get_datas()
