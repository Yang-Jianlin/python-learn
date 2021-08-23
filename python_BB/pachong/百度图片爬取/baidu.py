import requests
from lxml import etree
import os


def get_photo():
    url = 'https://pic.netbian.com/4kmeinv/'
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    }

    response_code = requests.get(url=url, headers=header).text
    print(response_code)
    tree = etree.HTML(response_code)

    li_list = tree.xpath('//ul[@class="clearfix"]/li')

    if not os.path.exists('photoLib'):
        os.mkdir('photoLib')

    for li in li_list:
        imageUrl = "https://pic.netbian.com/" + li.xpath('./a/img/@src')[0]
        imageName = li.xpath('./a/b/text()')[0] + '.jpg'
        img_name = imageName.encode('iso-8859-1').decode('gbk')

        imageData = requests.get(url=imageUrl, headers=header).content
        imagePath = 'photoLib/' + img_name
        with open(imagePath, 'wb') as fp:
            fp.write(imageData)
            print(img_name, '下载成功！！！')


if __name__ == '__main__':
    get_photo()
