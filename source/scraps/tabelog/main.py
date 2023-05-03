from module.my_selenium import *
from scraps.tabelog.constants import *
from selenium.webdriver.common.by import By


# d=get_driver()
d=load_driver()
d.get(start_page)

elems=d.find_elements(By.CLASS_NAME, "list-rst__rst-name-target")

links=[
    elem.get_attribute("href")
    for elem in elems
]



raise