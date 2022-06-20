import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time



# 특정한 여러가지 행위들으르 하나의 기능으로 사용하겠다는 의미
def rePlaceData(value):
    numbers = re.findall("\d+", value)
    result = ""
    for i in numbers:
        decodedNumber = i
        result += decodedNumber
    return result


def getAIAData(name, birth, gender):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    scrapingResult = {
        'company': "AIA",
        'price': 0,
        'contents': []
    }
    driver.implicitly_wait(3)
    driver.get(
        'https://www.aia.co.kr/ko/our-products/medical-protection/non-par-denteal-health-plan.html#')
    driver.implicitly_wait(3)
    textBox = driver.find_element(By.XPATH, value='//*[@id="aia644363719"]')
    textBox.send_keys("19"+birth)
    if gender == 1:
        femaleBtn = driver.find_element(By.XPATH, value=
            '//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]')
        femaleBtn.click()
    else:
        maleBtn = driver.find_element(By.XPATH, value=
            '//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[2]')
        maleBtn.click()
    resultBtn = driver.find_element(By.XPATH, value='//*[@id="btn806817556"]')
    resultBtn.click()
    driver.implicitly_wait(3)

    htmlResult = driver.find_element(By.XPATH, value=
        '//*[@id="premium-by-timespan-value"]').text
    resultValue = rePlaceData(htmlResult)
    print(resultValue)
    scrapingResult['price'] = resultValue
    tableBody = driver.find_element(By.XPATH, value=
        '//*[@id="collapse-large-724022276"]/div[1]/div/table').find_element(By.TAG_NAME, value='tbody')
    driver.find_element(By.XPATH, value=
        '//*[@id="the_fine_print"]/div[2]/div[1]/div[2]/div/a[2]').click()
    rows = tableBody.find_elements(By.TAG_NAME, value="tr")
    contentsList = []
    for index, value in enumerate(rows):
        if index != 0:
            print(value.find_elements(By.TAG_NAME, value='td')[0].text)
            contentsList.append(value.find_elements(By.TAG_NAME, value='td')[
                                0].text)
    scrapingResult['contents'] = contentsList
    time.sleep(10)
    return scrapingResult


def getLinaData(name, birth, gender):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    scrapingResult = {
        'company': "라이나",
        'price': 0,
        'contents': []
    }
    driver.get('https://direct.lina.co.kr/product/ess/dtc01/easy')
    textBox = driver.find_element(By.XPATH, value='//*[@id="birthday"]')
    textBox.send_keys(birth)
    if gender == 1:
        femaleBtn = driver.find_element(By.XPATH, value='//*[@id="main_btn_female"]')
        femaleBtn.click()
    else:
        maleBtn = driver.find_element(By.XPATH, value='//*[@id="main_btn_male"]')
        maleBtn.click()
    resultBtn = driver.find_element(By.XPATH, value=
        '//*[@id="btn_direct_dental_cal"]')
    resultBtn.click()
    driver.implicitly_wait(3)

    htmlResult = driver.find_element(By.XPATH, value=
        '//*[@id="contents"]/div[2]/div[2]/div[2]/div/table/tbody[1]/tr[1]/td[2]/strong').text
    resultValue = rePlaceData(htmlResult)
    scrapingResult['price'] = resultValue
    driver.implicitly_wait(2)
    detailBtn = driver.find_element(By.XPATH, value='//*[@id="openLayerplanPonA2"]')
    detailBtn.click()
    driver.implicitly_wait(2)

    tableBody = driver.find_element(By.XPATH, value=
        '//*[@id="planPonA2"]/div/div[2]/div/div/table[1]').find_element(By.TAG_NAME, value='tbody')
    rows = tableBody.find_elements(By.TAG_NAME, value="tr")
    contentsList = []
    for index, value in enumerate(rows):
        if index != 0:
            print(value.find_elements(By.TAG_NAME, value='th')[0].text)
            contentsList.append(value.find_elements(By.TAG_NAME, value='th')[
                                0].text)
    scrapingResult['contents'] = contentsList
    time.sleep(10)
    return scrapingResult



