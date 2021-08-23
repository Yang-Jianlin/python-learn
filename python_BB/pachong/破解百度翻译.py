import requests

if __name__ == '__main__':
    url = 'https://fanyi.baidu.com/sug'

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }

    kw = input('enter a word:')
    data = {
        'kw': kw
    }
    response = requests.post(url=url, data=data, headers=header)
    dic_obj = response.json()
    print(dic_obj)
