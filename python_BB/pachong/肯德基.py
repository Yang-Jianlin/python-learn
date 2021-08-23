import requests
import json
from python_BB.Tool import headerDict


def KenDeji():
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }

    raw_headers = """cname: 
pid: 
keyword: 秦皇岛
pageIndex: 1
pageSize: 10"""
    param = headerDict.header_dict(raw_headers)
    response = requests.post(url=url, data=param, headers=header)
    print(response.text)


if __name__ == '__main__':
    KenDeji()
