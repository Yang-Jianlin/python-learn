from python_BB.Tool import headerDict
import requests
from python_BB.pachong.药监局.userAgent import header
import json


def get_info():
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    ID = ''

    with open('info_id.txt', 'r', encoding='utf-8') as fp1:
        with open('info_all', 'w', encoding='utf-8') as fp2:
            while True:
                ID = fp1.readline()
                ID = ID[:len(ID)-1]
                # print(ID)
                if not ID:
                    break

                param = {
                    'id': ID
                }

                response = requests.post(url=url, headers=header, data=param)
                data_info = response.json()
                json.dump(data_info, fp=fp2, ensure_ascii=False)


if __name__ == '__main__':
    get_info()
