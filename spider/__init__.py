from selenium import webdriver
from time import sleep
import json


def browser_initial():
    browser = webdriver.Chrome(executable_path="../chromedriver") # 驱动路径 如果为window系统可能要加后缀.exe
    url = "https://now.qq.com/pcweb/story.html?roomid=1363586478&fromsource=searresult&_wv=16778245"
    return url, browser


def get_cookies(url, browser):
    """
    获取cookies保存到本地
    :param log_url:
    :param browser:
    :return:
    """
    browser.get(url)
    sleep(15)  # 扫码登录
    dict_cookies = browser.get_cookies()  # 获取cookie
    print(dict_cookies)
    json_cookies = json.dumps(dict_cookies)
    print(json_cookies)

    with open("cookie.txt", "w") as f:
        f.write(json_cookies)
    print("cookie 保存成功！")

if __name__ == "__main__":
    tur = browser_initial()
    get_cookies(tur[0], tur[1]) # 第一次访问扫码登录保存cookie

