import requests
from python_BB.Tool import headerDict
from python_BB.pachong.药监局.userAgent import header


def get_id():
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    raw_param = """on: true
page: 1
pageSize: 15
productName: 
conditionType: 1
applyname: 
applysn: """
    param = headerDict.header_dict(raw_param)
    pageNum = 1
    with open('info_id.txt', 'w', encoding='utf_8') as fp:
        while pageNum < 7:
            param['page'] = str(pageNum)
            pageNum += 1

            response = requests.post(url=url, headers=header, data=param)
            dataID = response.json()
            for i in dataID['list']:
                info = i['ID'] + '\n'
                fp.write(info)


if __name__ == '__main__':
    get_id()
