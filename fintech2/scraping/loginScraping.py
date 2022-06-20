from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get('https://www.leagueoflegends.com/ko-kr/')

#페이지 상호작용 위해 클릭, 키입력과 같은 이벤트 전달

loginButton = driver.find_element(By.XPATH, value='//*[@id="riotbar-right-content"]/div[3]/div[1]/a')
loginButton.click()

username = driver.find_element(By.NAME, value='username')
password = driver.find_element(By.NAME, value='password')

username.send_keys('test')
password.send_keys('test')

time.sleep(10)

