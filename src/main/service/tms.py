from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

def run():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://koritbs.cafe24.com/student/index.php")
    driver.maximize_window()
    sleep(1)

    usernameInput = driver.find_element(by=By.CSS_SELECTOR, value="body > div > form > table > tbody > tr:nth-child(3) > td > input")
    passwordInput = driver.find_element(by=By.CSS_SELECTOR, value="body > div > form > table > tbody > tr.border-left-danger.border-right-danger.border-bottom-0.border-top-0.bg-brown > td > input")
    # input에 입력하는 함수
    usernameInput.send_keys(os.getenv("TMS_USERNAME"))
    passwordInput.send_keys(os.getenv("TMS_PASSWORD"))

    loginButton = driver.find_element(by=By.CSS_SELECTOR, value="body > div > form > table > tbody > tr.border-left-danger.border-right-danger.border-bottom-danger.border-top-0.bg-brown > td > div > div:nth-child(2) > button")
    driver.execute_script("arguments[0].scrollIntoView(true);", loginButton)
    driver.execute_script("arguments[0].click();", loginButton) # 로그인 버튼 클릭
    sleep(3)