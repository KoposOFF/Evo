from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Укажите путь к драйверу Chrome
service = Service()

# Настройка опций для Chrome
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Убираем флаг автоматизации
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Отключаем автоматизацию

# Инициализация веб-драйвера с опциями
driver = webdriver.Chrome(service=service, options=chrome_options)

# Обновляем значение navigator.webdriver на false
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => false})")

# Открываем тестовый сайт
driver.get("https://bot.sannysoft.com/")  # Этот сайт проверяет, распознается ли бот

# Даем время на проверку
import time
time.sleep(25)

# Закрываем браузер
driver.quit()
