from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

base_url = ""

br = webdriver.Firefox()
br.get(base_url)

save_me = ActionChains(br).key_down(Keys.CONTROL).key_down('s').key_up(Keys.CONTROL).key_up('s')
save_me.perform()
