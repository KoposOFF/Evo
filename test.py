from selenium import webdriver
# from seleniumwire import webdriver
# from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv()
LOGIN = os.getenv("LOGIN")
PASS = os.getenv("PASS")
PROXY = os.getenv("PROXY")


def test_click():
    # option = webdriver.ChromeOptions()
    # option.add_argument(f"--proxy-server={PROXY}")
    option = {
    'proxy': {
            'http': f'http://{LOGIN}:{PASS}@{PROXY}',
            'https': f'https://{LOGIN}:{PASS}@{PROXY}',
            'no_proxy': 'localhost,127.0.0.1'  # Сайты, которые не должны использовать прокси
        }
    }
    browser = webdriver.Chrome(seleniumwire_options=option)
    
    browser.get("https://nseindia.com/")
    time.sleep(1)

    # browser.quit()

if __name__ == "__main__":
    test_click()
    print(LOGIN)
    print(PASS)
    print(PROXY)