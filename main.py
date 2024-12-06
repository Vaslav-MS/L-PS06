import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

url = 'https://tomsk.hh.ru/vacancies/programmist'
driver.get(url)
time.sleep(3)

vacas = driver.find_elements(By.CLASS_NAME, 'vacancy-info--ieHKDTkezpEj0Gsx')
parsed_data = []

for vac in vacas:
    try:
        title_element = vac.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_4-3-12')
        title = title_element.text
        link = title_element.get_attribute('href')
        company = vac.find_element(By.CSS_SELECTOR, 'span[data-qa="vacancy-serp__vacancy-employer-text"]').text
        try:
            salary = vac.find_element(By.CSS_SELECTOR, 'div.compensation-labels--vwum2s12fQUurc2J').find_element(By.CSS_SELECTOR, 'span').text
        except:
            salary = 'Не указана'
    except Exception as e:
        print(f'Произошла ошибка при парсинге: {e}')
        continue
    parsed_data.append([title, company, salary, link])

driver.quit()

with open('hh.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)
