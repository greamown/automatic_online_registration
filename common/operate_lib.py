from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from common.utils import element_present, alert_is_present, verfi_code_ocr

def login(driver: webdriver, email:str, id:str):
    # 抓取下拉選單元件
    select = Select(driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$apply_nation'))
    select.select_by_index(1)
    # Writting 
    driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$apply_sid').send_keys(id)
    driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$apply_email').send_keys(email)
    driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$vcode').send_keys(verfi_code_ocr(driver, "ContentPlaceHolder1_imgcode"))
    driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$btnappok').click()
    
def checking(driver: webdriver):
    driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$btnstepdown').click()
    driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$vcode2').send_keys(verfi_code_ocr(driver, "ContentPlaceHolder1_imgcode2"))
    driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$btnstep2downnext').click()
    
def result(driver: webdriver):
    driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$vcode').send_keys(verfi_code_ocr(driver, "ContentPlaceHolder1_imgcode"))
    driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$btnsave').click()
    time.sleep(2)

def first_step(driver: webdriver, email:str, id:str):
    login(driver, email, id)
    while True:
        # 如果有彈出框 點擊確定
        if alert_is_present(driver):
            driver.switch_to.alert.accept()
        btnupd = element_present(driver, 'ctl00$ContentPlaceHolder1$New_List$ctl00$btnupd')
        if not btnupd:
            driver.find_element(By.XPATH, "//a[@href='apply_2_1.aspx']").click()
            login(driver, email, id)
        else:
            break

    btnupd.click()
    time.sleep(1)
    if alert_is_present(driver):
        driver.switch_to.alert.accept()
        
def two_step(driver: webdriver):
    checking(driver)
    while True:
        # 如果有彈出框 點擊確定
        if alert_is_present(driver):
            driver.switch_to.alert.accept()
        btnsave = element_present(driver, "ctl00$ContentPlaceHolder1$btnsave")
        if not btnsave:
            driver.refresh()
            checking(driver)
        else:
            break
            
def final_step(driver: webdriver):
    result(driver)
    while True:
        # 如果有彈出框 點擊確定
        if alert_is_present(driver):
            driver.switch_to.alert.accept()
        btnPrint = element_present(driver, "ctl00$ContentPlaceHolder1$btnPrint")
        if not btnPrint:
            driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$vcode').clear()
            result(driver)
        else:
            break
