import requests
import json


def Douban():
    url = "https://movie.douban.com/j/chart/top_list"

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }

    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20'
    }

    repose = requests.get(url=url, params=param, headers=header)
    list_data = repose.json()

    with open('./douban.json', 'w', encoding='utf-8') as fp:
        json.dump(list_data, fp=fp, ensure_ascii=False)
    print(list_data)


if __name__ == '__main__':
    Douban()
