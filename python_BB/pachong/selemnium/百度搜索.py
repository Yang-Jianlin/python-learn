from selenium import webdriver
from time import sleep
bro = webdriver.Chrome(executable_path='./chromedriver.exe')

bro.get('https://www.baidu.com/')

search_input = bro.find_element_by_id("kw")
search_input.send_keys("汉")

btn = bro.find_element_by_id("su")
btn.click()
