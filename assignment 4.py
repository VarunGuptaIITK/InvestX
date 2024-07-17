import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

def scrape_option_chain(a,b):
    driver = webdriver.Chrome()
    driver.get('https://opstra.definedge.com')
    time.sleep(2)

    search_element = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/nav/div/div[4]/button/div')
    search_element.click()

    username = driver.find_element(By.XPATH, '//*[@id="username"]')
    username.send_keys("tamejoso0228@gmail.com")

    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    password.send_keys("Kprabhat@123")

    loginbutton = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    loginbutton.click()

    driver.get('https://opstra.definedge.com/strategy-builder')
    time.sleep(2)

    option_chain = driver.find_element(By.CSS_SELECTOR, '#app > div.application--wrap > main > div > div > div > div > div.home > div.container > div.layout > ul > li > div.v-expansion-panel__header > div.text-xs-center.title')
    time.sleep(2)
    option_chain.click()

    date_1_variable = driver.find_element(By.CSS_SELECTOR, a)
    date_1_variable.click()

    CallLTP = driver.find_elements(By.XPATH, '//tbody/tr/td[1]')
    itmprob = driver.find_elements(By.XPATH, '//tbody/tr/td[2]')
    CallIv = driver.find_elements(By.XPATH, '//tbody/tr/td[3]')
    CallDelta = driver.find_elements(By.XPATH, '//tbody/tr/td[4]')
    StrikePrice = driver.find_elements(By.XPATH, '//tbody/tr/td[5]')
    PutDelta = driver.find_elements(By.XPATH, '//tbody/tr/td[6]')
    PutIV = driver.find_elements(By.XPATH, '//tbody/tr/td[7]')
    ITMProb = driver.find_elements(By.XPATH, '//tbody/tr/td[8]')
    PutLTP = driver.find_elements(By.XPATH, '//tbody/tr/td[9]')
    

    option_data = []
    for i in range(len(StrikePrice)):
        try:
            row = {
                'CallLTP': CallLTP[i].text,
                'itmprob': itmprob[i].text,
                'CallIv': CallIv[i].text,
                'CallDelta': CallDelta[i].text,
                'StrikePrice': StrikePrice[i].text,
                'PutDelta': PutDelta[i].text,
                'PutIV': PutIV[i].text,
                'ITMProb': ITMProb[i].text,
                'PutLTP': PutLTP[i].text
            }
            option_data.append(row)
            print(row)
        except StaleElementReferenceException:
            time.sleep(2)
            CallLTP = driver.find_elements(By.XPATH, '//tbody/tr/td[1]')
            itmprob = driver.find_elements(By.XPATH, '//tbody/tr/td[2]')
            CallIv = driver.find_elements(By.XPATH, '//tbody/tr/td[3]')
            CallDelta = driver.find_elements(By.XPATH, '//tbody/tr/td[4]')
            StrikePrice = driver.find_elements(By.XPATH, '//tbody/tr/td[5]')
            PutDelta = driver.find_elements(By.XPATH, '//tbody/tr/td[6]')
            PutIV = driver.find_elements(By.XPATH, '//tbody/tr/td[7]')
            ITMProb = driver.find_elements(By.XPATH, '//tbody/tr/td[8]')
            PutLTP = driver.find_elements(By.XPATH, '//tbody/tr/td[9]')
            option_data.append(row)
            print(row)

    df = pd.DataFrame(option_data)
    print(df)

    # Corrected file path using raw string literal
    output_file = r'C:\Users\28pra\OneDrive\Desktop\project\FAC_project\New folder\{}.csv'.format(b)
    df.to_csv(output_file, index=False)

    driver.quit()


Date1='#app > div.application--wrap > main > div > div > div > div > div.home > div.container > div.layout > ul > li > div.v-expansion-panel__body > div.layout.justify-center.row.wrap > div:nth-child(1) > button > div'
Date2='#app > div.application--wrap > main > div > div > div > div > div.home > div.container > div.layout > ul > li > div.v-expansion-panel__body > div.layout.justify-center.row.wrap > div:nth-child(2) > button > div'
Date3='#app > div.application--wrap > main > div > div > div > div > div.home > div.container > div.layout > ul > li > div.v-expansion-panel__body > div.layout.justify-center.row.wrap > div:nth-child(3) > button > div'
Date4='#app > div.application--wrap > main > div > div > div > div > div.home > div.container > div.layout > ul > li > div.v-expansion-panel__body > div.layout.justify-center.row.wrap > div:nth-child(4) > button > div'
Date5='#app > div.application--wrap > main > div > div > div > div > div.home > div.container > div.layout > ul > li > div.v-expansion-panel__body > div.layout.justify-center.row.wrap > div:nth-child(4) > button > div'
d1='option_chain_data_27jul'
d2='option_chain_data_03aug'
d3='option_chain_data_10aug'
d4='option_chain_data_17aug'
d5='option_chain_data_31aug'


scrape_option_chain(Date1,d1)
scrape_option_chain(Date2,d2)
scrape_option_chain(Date3,d3)
scrape_option_chain(Date4,d4)
scrape_option_chain(Date5,d5)

