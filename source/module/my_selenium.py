from module.constants import *

from selenium import webdriver



def get_driver():
    driver=None
    try:
        driver=load_driver()
    except:
        print("exception in load driver")
        install_driver()
        driver=load_driver()
    try:
        driver.get("https://google.com/")
    except:
        print("exception in test")
        install_driver()
        driver=load_driver()
    return driver

def load_driver():
    with open(driver_path_file, "r", encoding="utf-8") as f:
        path=f.read()        
    options=webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={user_data_dir}") #Path to your chrome profile
    options.add_argument(f"--profile-directory={profile_directory}")
    options.add_argument('disable-notifications')
    driver=webdriver.Chrome(path,options=options)
    return driver

def install_driver():    
    print("install driver")
    from webdriver_manager.chrome import ChromeDriverManager
    path=ChromeDriverManager().install()

    with open(driver_path_file, "w", encoding="utf-8") as f:
        f.write(path)
