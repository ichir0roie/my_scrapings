import os
from module.constants import *

folders=[
    "data/input",
    "data/output",
    "settings/driver"
]

for folder in folders:
    os.makedirs(folder,exist_ok=True)



# 最新のドライバーのインストール。

from webdriver_manager.chrome import ChromeDriverManager
path=ChromeDriverManager().install()

with open(driver_path_file, "w", encoding="utf-8") as f:
    f.write(path)



