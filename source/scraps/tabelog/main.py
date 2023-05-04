from pandas import *
from module.my_selenium import *
from scraps.tabelog.constants import *
from selenium.webdriver.common.by import By


# d=get_driver()
d = load_driver()
d.get(start_page)

elements = d.find_elements(By.CLASS_NAME, "list-rst__contents")

info_list = []


def find_text(e, class_name):
    try:
        return e.find_element(By.CLASS_NAME, class_name).text
    except:
        return ""


for e in elements:
    title_elem = e.find_element(By.CLASS_NAME, "list-rst__rst-name-target")
    title = title_elem.text
    kind = find_text(e, "list-rst__area-genre")
    star = find_text(e, "c-rating__val")
    money = find_text(e, "c-rating-v3__val")
    link = title_elem.get_attribute("href")
    desc = find_text(e, "list-rst__pr-title")

    info = [
        title,
        money,
        star,
        kind,
        desc,
        link,
    ]
    info_list.append(info)

    pass

DataFrame(info_list).to_csv(
    "data/output/tabelog.tsv",
    sep="\t", index=False, header=[
        "title",
        "money",
        "star",
        "kind",
        "desc",
        "link",
    ]
)

raise
