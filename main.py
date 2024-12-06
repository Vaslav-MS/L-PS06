import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

url = 'https://www.divan.ru/ekaterinburg/category/svet'
driver.get(url)
time.sleep(1)

parsed_data = []

svetis = driver.find_elements(By.CSS_SELECTOR, 'div.lsooF')

for svet in svetis:
    try:
        name = svet.find_element(By.CSS_SELECTOR, 'a').text
        url = svet.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        price = svet.find_element(By.CSS_SELECTOR, 'span.KIkOH').text

    except Exception as e:
        print(f'Произошла ошибка при парсинге: {e}')
        continue
    parsed_data.append([name, price, url])

driver.quit()

with open('svet.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)
