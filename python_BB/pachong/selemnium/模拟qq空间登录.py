from selenium import webdriver
from python_BB.pachong.selemnium.chaojiying_Python import chaojiying
import requests
from lxml import etree
from selenium.webdriver import ChromeOptions
import time


class QQLogin:
    def __init__(self, userName, userPasswd):
        self.userName = userName
        self.userPasswd = userPasswd

        # 实现规避检测
        option = ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 如何实现让selenium规避被检测到的风险
        self.bro = webdriver.Chrome(executable_path='chromedriver.exe', options=option)
        self.bro.get('https://qzone.qq.com/')
        self.bro.switch_to.frame('login_frame')
        self.div = self.bro.find_element_by_id('switcher_plogin')
        self.div.click()

    def get_coordinate(self):
        page_text = self.bro.page_source
        tree = etree.HTML(page_text)
        # code_url = tree.xpath('//*[@id="slideBg"]/@src')[0]
        print(page_text)

    def login_qq(self):
        time.sleep(0.5)

        user_name = self.bro.find_element_by_id('u')
        user_passwd = self.bro.find_element_by_id('p')
        user_name.send_keys('1494237426')
        time.sleep(0.5)
        user_passwd.send_keys('ylovew20171130')
        time.sleep(0.5)

        btn_click = self.bro.find_element_by_id('login_button')
        btn_click.click()

        self.bro.switch_to.frame('login_frame')
        page_text = self.bro.page_source
        tree = etree.HTML(page_text)
        # code_url = tree.xpath('//*[@id="slideBg"]/@src')[0]
        print(page_text)


if __name__ == '__main__':
    userName = '1494237426'
    userPasswd = 'ylovew20171130'
    qqlogin = QQLogin(userName, userPasswd)
    qqlogin.login_qq()
