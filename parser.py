import requests
from bs4 import BeautifulSoup


COM_URL = f"http://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=ai&dum=dum&boardId=43626718"
"&page={page}&command=list"
"&page={page}&command=list"


def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    print(soup)


def get_data(board_id):
    url = f"http://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=ces&dum=dum&boardId={board_id}"
    last_page = get_last_page(url)


def main():
    ai_board_id = "150797968"
    com_board_id = "43626718"
    get_ai_data = get_data(ai_board_id)


main()
