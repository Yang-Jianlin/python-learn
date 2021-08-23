"""
解析出58二手房源信息的名称，价格和面积
https://qhd.58.com/ershoufang
"""

import requests
from lxml import etree


def get_info():
    url = "https://qhd.58.com/ershoufang/"

    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    }

    response_code = requests.get(url=url, headers=header).text
    print(response_code)

    tree = etree.HTML(response_code)
    div_list = tree.xpath('//section[@class="list"]/div')
    # print(div_list)

    for div in div_list:
        print('11')
        title = div.xpath('./div[@class="property-content"]//'
                          'div[@class="property-content-title"]/h3/text()')
        print(title)


if __name__ == '__main__':
    get_info()
