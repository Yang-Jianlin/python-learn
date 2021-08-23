from selenium import webdriver
from lxml import etree
from time import sleep
from selenium.webdriver import ChromeOptions

# 实现规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

# 实例化一个浏览器对象（传入浏览器的驱动成）
bro = webdriver.Chrome(executable_path='chromedriver.exe', options=option)
# 让浏览器发起一个指定url对应请求
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

# page_source获取浏览器当前页面的页面源码数据
page_text = bro.page_source
print(page_text)

# tree = etree.HTML(page_text)
# li_list = tree.xpath('/html/@xmlns')
# print(li_list)
