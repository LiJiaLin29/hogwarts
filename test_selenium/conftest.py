"""
 @description: fixture,供多个test文件使用
 @auther: 29263
 @date: 2020-08-22 14:47
"""
import os
import shelve, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def login_winxin(driver):
    """
    从shelve文件获取cookies，登录企业微信
    """
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    time.sleep(3)
    # 获取cookies
    with shelve.open("./data/cookies-weixin") as s:
        cookies = s["cookies"]
        for cookie in cookies:  # 遍历列表
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            driver.add_cookie(cookie)


def prepare_login(name, url):
    """
    复用chrome浏览器 端口：9222，需要人为提前在浏览器登录
    并使用shelve将cookies持久化到本地
    """
    # 检查cookies文件是否存在
    fpath = f"./data/cookies-{name}"
    if (not os.path.exists(fpath)) or (os.path.exists(fpath)
                                       and os.path.getsize(fpath) == 0):
        option = Options()
        option.debugger_address = "localhost:9222"
        driver = webdriver.Chrome(options=option)
        driver.get(url)
        with shelve.open(fpath) as s:
            s["cookies"] = driver.get_cookies()  # 将cookies存到文件
            print("保存cookies：", s["cookies"])
        driver.close()


if __name__ == "__main__":
    # 调用prepare_login，获取企业微信cookies
    prepare_login("weixin", "https://work.weixin.qq.com/wework_admin/frame#index")





