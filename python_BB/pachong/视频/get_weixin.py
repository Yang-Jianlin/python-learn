import requests

url = 'https://mpvideo.qpic.cn/0bf2zqafoaaapqahp6q3szqvbtgdk7gaavya.f10002.mp4?dis_k=4328ef373216afc8a5e434e768d7cf28&dis_t=1629549371&vid=wxv_2006144357283741700&format_id=10002&support_redirect=0&mmversion=false'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

with open('W_video.mp4', 'wb') as fp:
    fp.write(requests.get(url=url, headers=headers).content)
