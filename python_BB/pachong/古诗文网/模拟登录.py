import requests
import code_idendity
from lxml import etree


def get_randcode():
    url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    }

    response = requests.get(url=url, headers=headers)
    response.encoding = "utf-8"
    response = response.text

    tree = etree.HTML(response)
    img_url = "https://so.gushiwen.cn/" + tree.xpath('//*[@id="imgCode"]/@src')[0]

    img_data = requests.get(url=img_url, headers=headers).content
    with open('img.jpg', 'wb') as fp:
        fp.write(img_data)

    img_path = "E:\python数据结构与算法\python_BB\pachong\古诗文网\img.jpg"
    result = code_idendity.base64_api(uname='ymumu', pwd='yjl970924', img=img_path, typeid=3)
    print(result)
    return result


def login(code):
    url = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    }

    prarm = {
        '__VIEWSTATE': 'G2iPPeafvJB / wVJK64ak9ESR72O7t0nCRFT1btk + TK19f4H5EiinLpvxWivHqWb3TzUqO05Z6GjtEP0FU1PahnvD8IA9om4ZvXBpLGrrVJe9LAeIiHlNCgxygW4 =',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': '13237619093',
        'pwd': 'yjl970924',
        'code': code,
        'denglu': '登录'
    }

    response = requests.post(url=url, headers=headers, data=prarm)
    with open('login.html', 'w', encoding='utf-8') as fp:
        fp.write(response.text)
    print(response.status_code)


def get_randcode2():
    url = "http://www.ttshitu.com/login.html?spm=null"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    }

    response = requests.get(url=url, headers=headers)
    response.encoding = "utf-8"
    response = response.text
    with open('response.html', 'w', encoding='utf-8') as fp:
        fp.write(response)

    tree = etree.HTML(response)
    img_url = tree.xpath('//*[@id="captchaImg"]/@src')[0]
    print('url=', img_url)

    # img_data = requests.get(url=img_url, headers=headers).content
    # with open('img.jpg', 'wb') as fp:
    #     fp.write(img_data)
    #
    # img_path = "E:\python数据结构与算法\python_BB\pachong\古诗文网\img.jpg"
    # result = code_idendity.base64_api(uname='ymumu', pwd='yjl970924', img=img_path, typeid=1)
    # print(result)
    # return result


def login2(code):
    url = "http://admin.ttshitu.com/common/api/login/user"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    }

    prarm = {
        'userName': "ymumu",
        'password': "yjl970924",
        'captcha': code,
        'imgId': "7bcb36f18d384cc6b05d6a58296ff92c",
        'developerFlag': 'false',
        'needCheck': 'true'
    }

    response = requests.post(url=url, headers=headers, data=prarm)
    with open('login.html', 'w', encoding='utf-8') as fp:
        fp.write(response.text)
    print(response.status_code)


if __name__ == '__main__':
    get_randcode2()


