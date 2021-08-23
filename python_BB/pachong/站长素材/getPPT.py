"""
获取站长素材里面的免费ppt模板
https://sc.chinaz.com/ppt/free.html
"""

import requests
import os
from lxml import etree


def get_ppt():
    # 先获取首页的html源码，每个ppt展示框对应下载界面地址，需要先获取下载界面地址
    url = 'https://sc.chinaz.com/ppt/free.html'
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    }

    home_page = requests.get(url=url, headers=header)
    home_page.encoding = 'utf-8'  # 防止html显示乱码
    home_page = home_page.text

    tree = etree.HTML(home_page)
    div_list = tree.xpath('//div[@class="ppt-list "]/div')

    # 创建文件夹用于保存获得的ppt模板
    if not os.path.exists('pptLib'):
        os.mkdir('pptLib')

    for div in div_list:
        div_url = 'https://sc.chinaz.com' + div.xpath('./div[@class="bot-div"]/a/@href')[0]
        ppt_name = div.xpath('./div[@class="bot-div"]/a/text()')[0] + '.rar'

        # 获取下载页的源码内容并解析出下载地址
        download_page = requests.get(url=div_url, headers=header)
        download_page.encoding = 'utf-8'
        download_page = download_page.text

        down_tree = etree.HTML(download_page)
        down_addr = down_tree.xpath('//div[@class="download-url"]/a[1]/@href')[0]
        ppt_data = requests.get(url=down_addr, headers=header).content
        pptName = 'pptLib/' + ppt_name
        with open(pptName, 'wb') as fp:
            fp.write(ppt_data)
            print(pptName, '下载成功！！！')


if __name__ == '__main__':
    get_ppt()
