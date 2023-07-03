from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Initialize the Chrome browser
message = input("write the message: ")
photo_path = input("write the path: ")
driver = webdriver.Chrome()
# Navigate to a website
driver.get("https://twitter.com/")

def sender():
    
    with open("twitter_usersname.txt", "r") as file:
            lines = file.readlines()
            while lines:
                for i in range(1):
                    try:
                        driver.get("https://twitter.com/messages/compose")
                        time.sleep(4)
                        search =driver.find_elements(By.XPATH , "//input[@type='text']")
                        search[0].send_keys(lines[0])
                        lines.pop(0)
                        time.sleep(2)
                        with open("twitter_usersname.txt", "w") as file:
                            file.writelines(lines)
                        target = driver.find_elements(By.XPATH , "//div[@class='css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci']")
                        target[0].click()
                        time.sleep(2)
                        next_button = driver.find_element(By.XPATH , "//span[text()='Next']")
                        next_button.click()
                        time.sleep(4)
                        photo = driver.find_element(By.XPATH , "//input[@type='file']")
                        photo.send_keys(photo_path)
                        time.sleep(10)
                        start_message = driver.find_element(By.XPATH , "//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
                        start_message.send_keys(message)
                        time.sleep(2)
                        send = driver.find_element(By.XPATH , "//div[@aria-label='Send']")
                        send.click()
                        time.sleep(2)
                    except:
                         next



sender()
