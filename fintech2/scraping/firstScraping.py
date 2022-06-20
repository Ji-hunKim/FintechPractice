from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get('https://www.mk.co.kr/news/world/view/2022/06/533563/?utm_source=naver&utm_medium=newsstand')

title = driver.find_element(By.XPATH, value='//*[@id="top_header"]/div/div/h1')
print(title.text)
subtitle = driver.find_element(By.XPATH, value='//*[@id="top_header"]/div/div/h2')
print(subtitle.text)
tfcn = driver.find_element(By.CLASS_NAME, "top_title")
print(tfcn.text)