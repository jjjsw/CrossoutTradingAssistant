from bs4 import BeautifulSoup
import re
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
#chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

url = 'https://crossoutdb.com/'
driver.get(url)

#click rarity dropdown button:
driver.find_element(By.XPATH,"//button[@id='rarityDropdown']").click()

#choose rarity: a[3] means 3rd dropdown option: special
driver.find_element(By.XPATH,"//div[@class='dropdown-menu show']/a[1]").click()

#click 'crafting' button:
driver.find_element(By.XPATH,"//button[@id='craftingPreset']").click()

#click category dropdown; choose cabin, weapon, hardware, movement:
driver.find_element(By.XPATH,"//button[@id='categoryDropdown']").click()
driver.find_element(By.XPATH,"//div[@class='dropdown-menu show']/a[1]").click()
driver.find_element(By.XPATH,"//div[@class='dropdown-menu show']/a[2]").click()
driver.find_element(By.XPATH,"//div[@class='dropdown-menu show']/a[3]").click()
driver.find_element(By.XPATH,"//div[@class='dropdown-menu show']/a[4]").click()

datas = []
numOfTables = int(len(driver.find_elements(By.XPATH,
"//li[@class='paginate_button page-item ' or @class='paginate_button page-item active']"))/2)

uncraftableItems = ['M-25 Guardian','AC62 Therm','Tempest','Median','Pyralid','Tempura','Emily','Summator',
                    'Array','Array ST','KA-1 Discharger','Camber','Camber ST','Iris','Omni','Hermit','Hermit ST',
                    'Averter','Gremlin','Yaoguai','Thresher','Whirl','Argument','Buggy wheel','Buggy wheel ST',
                    'Nest','Trigger','Trombone','Miller','Gravastar','Blockchain','Jannabi','Gungnir','Verifier',
                    'Bootstrap','KA-2 Flywheel','Aggressor','Omnibox','Sleipnir','Bigram','Enlightenment']

#loop all pages
for i in range(0, numOfTables):

    #extract data from table in CURRENT page:
    table = driver.find_element(By.XPATH,"//tbody")
    tableInnerHTML = table.get_attribute('innerHTML')
    newTable = BeautifulSoup(tableInnerHTML, 'html.parser')
    rows = newTable.find_all('tr')
    time.sleep(0.5)

    for row in rows:
        itemName = row.find_all('td')[0].text
        if itemName in uncraftableItems:
            continue

        itemHREF = "/item/" + row.find_all('td')[1].text
        #go to each item page
        driver.execute_script("arguments[0].click();", 
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='" + itemHREF + "']"))))

        #go to crafting section 
        driver.execute_script("arguments[0].click();", 
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Crafting')]"))))

        #click 'all sell'
        driver.execute_script("arguments[0].click();", 
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, 
        "//button[@class='btn btn-sm btn-outline-secondary root-price-select-sell-btn ']"))))

        #check optimal route profit
        driver.execute_script("arguments[0].click();", 
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, 
        "//button[@class='btn btn-outline-secondary btn-sm optimal-route-btn mr-1']"))))
        optimalRouteProfit = float(driver.find_element(By.XPATH,"//div[@class='sum-pos' or @class='sum-neg']").text)

        #check expand-all profit
        driver.execute_script("arguments[0].click();", 
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, 
        "//button[@class='btn btn-outline-secondary btn-sm expand-all-btn']"))))
        expandAllProfit = float(driver.find_element(By.XPATH,"//div[@class='sum-pos' or @class='sum-neg']").text)

        #if both profit <0, ignore this item. else, get highest profit
        if optimalRouteProfit <= 0 and expandAllProfit <= 0:
            driver.back()
            continue
        elif (optimalRouteProfit > expandAllProfit) or (optimalRouteProfit == expandAllProfit):
            profit = optimalRouteProfit
            method = 'optimalRoute'
        elif expandAllProfit > optimalRouteProfit:
            profit = expandAllProfit
            method = 'expandAll'

        driver.back()
        time.sleep(0.2)
        data = {
            'name': itemName,
            'profit': profit,
            'method': method,
            'demand/supply': round(float(row.find_all('td')[17].text.strip('%'))/100, 2),
        }
        datas.append(data)

    #go next page unless on end page
    if i+1 < numOfTables:
        driver.execute_script("arguments[0].click();", 
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='paginate_button page-item next']"))))

print(sorted(datas, key=lambda d: d['profit'], reverse=True))

driver.close()