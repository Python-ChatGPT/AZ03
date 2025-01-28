from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import matplotlib.pyplot as plt
import csv

driver = webdriver.Firefox()

# Page URL
url = 'https://www.divan.ru/category/divany'

print("Opening target page...")
driver.get(url)

# Waiting some time for the page to be fully loaded
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div._Ud0k"))
    )
finally:
    pass

print("Parsing data...")
divans = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')
parsed_data = []
for divan in divans:
    name = divan.find_element(By.CSS_SELECTOR, 'div.lsooF span[itemprop=name]').text
    price = int(divan.find_element(By.CSS_SELECTOR, 'div.lsooF meta[itemprop=price]').get_attribute('content'))
    url = divan.find_element(By.CSS_SELECTOR, 'div.lsooF a.qUioe').get_attribute('href')
    parsed_data.append([name, price, url])

print("Writing data to CSV file...")
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price', 'URL'])
    writer.writerows(parsed_data)

driver.quit()

print("Loading data from CSV file with pandas...")
file_path = 'prices.csv'
data = pd.read_csv(file_path)
prices = data['Price']

print("Building histogram...")
plt.hist(prices, bins=10, edgecolor='black')

# Adding histogram title and captions for the axes
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

print("Showing histogram")
plt.show()

print("Bye!")
