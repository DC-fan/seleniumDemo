import selenium
from selenium import webdriver
from time import sleep
import json


def browser_initial():
    browser = webdriver.Chrome(executable_path="../chromedriver") # 驱动路径 如果为window系统可能要加后缀.exe
    url = "https://now.qq.com/pcweb/story.html?roomid=1363586478&fromsource=searresult&_wv=16778245"
    return url, browser


def login_load(url, browser):
    """
    从本地读取cookie登录页面
    :param browser:
    :return:
    """

    browser.get(url)

    with open("cookie.txt", "r", encoding="utf-8") as f:
        list_cookie = json.loads(f.read())

    for cookie in list_cookie:
        # print(cookie)
        cookie_dict = {
            'domain': 'now.qq.com',
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            "expires": '',
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False
        }
        browser.add_cookie(cookie_dict)

    # 刷新页面
    browser.refresh()

    # 等待加载所有的元素
    sleep(5)

    try:
        # 获取输入框
        massage_input = browser.find_element_by_class_name('message-input')
        massage_input.send_keys("test")
        # 获取确定按钮
        message_send_btn = browser.find_element_by_class_name("message-send-btn")
        # 单击
        message_send_btn.click()
        # 等待3秒退出,为了观察到回复的效果
        sleep(3)
    except selenium.common.exceptions.NoSuchElementException as e:
        print("获取输入框错误")
        print(e)
    finally:
        # 退出
        browser.quit()


if __name__ == "__main__":
    tur = browser_initial()
    # get_cookies(tur[0], tur[1]) 第一次访问扫码登录保存cookie
    login_load(tur[0], tur[1])
