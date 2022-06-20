from tkinter.simpledialog import SimpleDialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://eum.go.kr/web/am/amMain.jsp')

# select이벤트 처리위해 select로 캐스팅(묶어줌) -> select 기능 사용가능
selsido = Select(driver.find_element(By.XPATH, value='//*[@id="selSido"]'))
selsido.select_by_visible_text('서울특별시')
# 중간에 서버가 군구를 찾기 위해 통신해야하기 때문에 대기시간 필요
driver.implicitly_wait(1)

selsgg = Select(driver.find_element(By.XPATH, value='//*[@id="selSgg"]'))
selsgg.select_by_visible_text('강남구')
driver.implicitly_wait(1)

dong = Select(driver.find_element(By.XPATH, value='//*[@id="selUmd"]'))
dong.select_by_visible_text('삼성동')
driver.implicitly_wait(1)

bobn = driver.find_element(By.XPATH, value=
    '//*[@id="bobn"]')
bubn = driver.find_element(By.XPATH, value=
    '//*[@id="bubn"]')

bobn.send_keys('45')
bubn.send_keys('1')

button = driver.find_element(By.XPATH, value=
    '//*[@id="frm"]/fieldset/div[3]/p/span/a')
button.click()

price = driver.find_element(By.XPATH, value=
    '//*[@id="appoint"]/div[2]/table/tbody/tr[3]/td')
print(price.text)

driver.implicitly_wait(1)
