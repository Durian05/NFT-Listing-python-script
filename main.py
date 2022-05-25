import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
def check_exists_by_xpath(driver):
    try:
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[text() = 'Cancel ']")
    except NoSuchElementException:
        return False
    return True
def cansel_list(driver,i):
    try:
        # element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/div/div/div[2]/div[1]/div/div[1]/div[2]/section[1]/div/div[2]/div/button[1]")))
        # driver.find_element(By.XPATH,"//*[@id='main']/div/div/div[2]/div[1]/div/div[1]/div[2]/section[1]/div/div[2]/div/button[1]").click()
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Cancel ']")))
        driver.find_element(By.XPATH, "//*[text() = 'Cancel ']").click()
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Confirm']")))
        driver.find_element(By.XPATH, "//*[text() = 'Confirm']").click()
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Sign']")))
        driver.find_element(By.XPATH, "//*[text() = 'Sign']").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//*[text() = 'Подписать']")))
        driver.find_element(By.XPATH,"//*[text() = 'Подписать']").click()
        driver.switch_to.window(driver.window_handles[0])
    except NoSuchElementException:
        print("нет кнопки",i)
        return
    except ElementClickInterceptedException:
        print("кликнул",i)
        return
    except TimeoutException:
        print("время cancel list",i)
        return
    return
def sell(driver,i):
    try:
        # element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/div/div/div[2]/div[1]/div/div[1]/div[2]/section[1]/div/div[2]/div/button[1]")))
        # driver.find_element(By.XPATH,"//*[@id='main']/div/div/div[2]/div[1]/div/div[1]/div[2]/section[1]/div/div[2]/div/button[1]").click()
        element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Sell']")))
        driver.find_element(By.XPATH, "//*[text() = 'Sell']").click()
        element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'// *[ @ id = "main"] / div / div / div[3] / div / div[2] / div / div[1] / form / div[1] / div / div[2] / div / div / div[2] / input')))
        driver.find_element(By.XPATH,'// *[ @ id = "main"] / div / div / div[3] / div / div[2] / div / div[1] / form / div[1] / div / div[2] / div / div / div[2] / input').send_keys(raa(a))
        element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Complete listing']")))
        driver.find_element(By.XPATH, "//*[text() = 'Complete listing']").click()
        element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Sign']")))
        driver.find_element(By.XPATH, "//*[text() = 'Sign']").click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Подписать']")))
        driver.find_element(By.XPATH, "//*[text() = 'Подписать']").click()
        driver.switch_to.window(driver.window_handles[0])
    except NoSuchElementException:
        print("нет кнопки",i)
        return
    except ElementClickInterceptedException:
        print("кликнул",i)
        return
    except TimeoutException:
        print("время sell",i)
        return
    return
def raa(a):
    return a[random.randint(0,2)]
a = ["0.0025","0.0035","0.0045"] ## set price

options = webdriver.ChromeOptions()
options.add_extension(r"C:\Users\danmo\PycharmProjects\pythonProject1\metamaskExtension.crx")
chrome_driver_binary = r'C:\bin\chromedriver.exe'
driver = webdriver.Chrome(executable_path= r'C:\bin\chromedriver.exe', options=options )
driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome')
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[3]/div/div/div/button').click()
driver.find_element(By.XPATH,"//*[text() = 'Импортировать кошелек']").click()
driver.find_element(By.XPATH,"//*[text() = 'Я согласен']").click()
time.sleep(2)
inputs = driver.find_elements(By.XPATH,'//input')
inputs[0].send_keys("") ##specify your mnemonic phrase
inputs[1].send_keys("")##enter your password
inputs[2].send_keys("")##enter your password

driver.find_element(By.CSS_SELECTOR,'.first-time-flow__terms').click()
driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[3]/div/div/form/button').click()
time.sleep(1)
driver.get('https://opensea.io')
if 4 == int(input()):
    start_time = time.time()
    for i in range(11612,20000):
        driver.get('https://opensea.io/assets/matic/0x0af107fe0350418d155e1a9feb2a34a858d45268/'+str(i)) ## specify the directory
        if check_exists_by_xpath(driver) == True:
            cansel_list(driver,i)
            sell(driver,i)
        else:
            sell(driver,i)
        # element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'refresh']")))
        # driver.find_element(By.XPATH, "//*[text() = 'refresh']").click()
        # time.sleep(1)
        # driver.refresh()
        # time.sleep(1)

    print("--- %s seconds ---" % (time.time() - start_time))