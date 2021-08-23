import requests

if __name__ == '__main__':
    url = 'https://www.sogou.com/web'

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }

    kw = input('enter a word:')
    param = {
        'query': kw
    }
    response = requests.get(url=url, params=param, headers=header)
    page_text = response.text
    filename = kw + '.html'
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('save success!')
