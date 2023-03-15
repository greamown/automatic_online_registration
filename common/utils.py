import cv2, ddddocr
import numpy as np
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

IMAGE_PAHT = "docs/cv2.png"
CAPTURE = "docs/capture.png"

def verfi_code_ocr(driver: webdriver, ID:str) -> str:
    element = driver.find_element(By.ID, ID)
    data = element.screenshot_as_png
    decoded = cv2.imdecode(np.frombuffer(data, np.uint8), 1)
    cv2.imwrite(IMAGE_PAHT, decoded)
    from PIL import Image
    img = Image.open(IMAGE_PAHT)
    imgry = img.convert('L')
    _, threshold = cv2.threshold(np.array(imgry), 140, 255, cv2.THRESH_BINARY)
    img = Image.fromarray(threshold)
    
#     # 灰階處理
#     gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
#     _, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
#     # 雜訊處理
#     noise = np.random.normal(0, 15, threshold.shape)
#     noise = np.clip(threshold +noise, 0, 255).astype('uint8')
#     guassian = cv2.blur(noise, (3, 3))
#     img = Image.fromarray(guassian)

    # 最後存回 PIL Image
    img.save(CAPTURE)
    ocr = ddddocr.DdddOcr()
    return ocr.classification(img)

def element_present(driver: webdriver, key:str):
    try:
        element = driver.find_element(By.NAME, key)
    except NoSuchElementException as e:
        return False
    return element

# 判斷是否有彈出框
def alert_is_present(driver: webdriver):
    try:
        alert = driver.switch_to.alert
        print(alert.text)
        return alert
    except:
        return False