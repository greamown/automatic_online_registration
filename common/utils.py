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
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    blur = cv2.medianBlur(img, 3)
    cv2.imshow("docs/blur.jpg", blur)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    cv2.imshow("docs/gray.jpg", gray)
    gray = cv2.fastNlMeansDenoising(gray, None, 40, 7, 21)
    cv2.imshow("docs/noise.jpg", gray)
    _, threshold = cv2.threshold(np.array(gray), 140, 255, cv2.THRESH_BINARY)
    cv2.imshow("dTHRESH_BINARY_INV", threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    img = Image.fromarray(threshold)

    # 最後存回 PIL Image
    img.save(CAPTURE)
    ocr = ddddocr.DdddOcr(show_ad=False)
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