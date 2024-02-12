from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = r"мой путь к chromedriver"

# Создаем экземпляр Options
options = Options()

# Создаем экземпляр Service и передаем путь к драйверу
service = Service(executable_path=driver_path)

# Инициализируем драйвер с указанными опциями и сервисом
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.google.ru')

# Явное ожидание появления кнопки принятия cookies
try:
    accept_cookies_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "L2AGLb"))
    )
    accept_cookies_button.click()
    print("Уведомление о cookies было закрыто.")
except Exception as e:
    print("Уведомление о cookies не было найдено или не удалось его закрыть.")

# Ожидание, чтобы убедиться, что страница полностью загружена
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))

# Находим элемент поисковой строки по имени
search_box = driver.find_element(By.NAME, 'q')

# Ввод текста для поиска и нажатие Enter
search_box.send_keys('Selenium')
search_box.send_keys(Keys.RETURN)

# Явное ожидание для отображения результатов поиска
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'search')))

time.sleep(5) # Дополнительное время для просмотра результатов

driver.quit()
