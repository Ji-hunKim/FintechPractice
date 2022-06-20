from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#크롬을 통해서 스크래핑을 진행, 크롬 드라이버 로딩

driver.get('https://www.melon.com/chart/')

tablebody = driver.find_element(By.XPATH, value='//*[@id="frm"]/div/table/tbody')
rowintable = tablebody.find_elements(By.TAG_NAME, value='tr')
for index, row in enumerate(rowintable):
    print(index + 1)
    titleAndSinger = row.find_elements(By.TAG_NAME, value='td')[5] #6번째 칼럼 선택해서 표시
    print(titleAndSinger.text)


