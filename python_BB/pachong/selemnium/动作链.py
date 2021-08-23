from selenium import webdriver
import time

from selenium.webdriver import ActionChains
bro = webdriver.Chrome(executable_path='chromedriver.exe')

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

bro.switch_to.frame('iframeResult')
div = bro.find_element_by_id('draggable')

action = ActionChains(bro)
action.click_and_hold(div)

for i in range(5):
    action.move_by_offset(10, 0).perform()
    time.sleep(0.5)

action.release()
