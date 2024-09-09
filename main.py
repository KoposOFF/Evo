from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import zipfile
import time
import os
from dotenv import load_dotenv

load_dotenv()

PROXY_HOST = os.getenv("IP") # rotating proxy or host
PROXY_PORT = os.getenv("PORT") # proxy port
PROXY_USER = os.getenv("LOGIN") # username
PROXY_PASS = os.getenv("PASS") # password

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["localhost"]
        }
    };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)


def get_chromedriver(use_proxy=False, user_agent=None):
    chrome_options = webdriver.ChromeOptions()

    if use_proxy:
        # chrome_options.add_argument('--proxy-server=your_proxy:proxy_port')

        plugin_file = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(plugin_file, 'w') as zp:
            zp.writestr('manifest.json', manifest_json)
            zp.writestr('background.js', background_js)

        chrome_options.add_extension(plugin_file)

    if user_agent:
        chrome_options.add_argument(f'--user-agent={user_agent}')

    driver = webdriver.Chrome(options=chrome_options)

    return driver


def main():
    driver = get_chromedriver(use_proxy=False, user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36')
    cookies = driver.get_cookies()
    driver.delete_all_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie) # добавление сессии решило проблему с подгрузкой котировок в таблицу

    driver.get('https://www.nseindia.com/')
    # time.sleep(3)
    marker = driver.find_element(By.ID, 'link_2')
    actions = ActionChains(driver)
    actions.move_to_element(marker).perform()
    time.sleep(5)
    link = driver.find_element(By.LINK_TEXT, "Pre-Open Market")
    link.click()
 

    time.sleep(20)

    driver.quit()


if __name__ == '__main__':
    main()