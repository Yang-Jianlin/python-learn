import requests


if __name__ == '__main__':
    url = 'https://www.sogou.com/web?query=%E8%BF%88%E5%85%8B%E5%B0%94'
    response = requests.get(url)
    print(response.text)

    with open('sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(response.text)

