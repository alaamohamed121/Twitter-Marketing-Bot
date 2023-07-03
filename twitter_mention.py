from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# Initialize the Chrome browser
driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://twitter.com/")

post = input("Enter post link: ")

def mention():
    driver.get(post)
    time.sleep(10)
    while True:
        try:
            writePbutton = driver.find_element(By.XPATH , "//div[@class='DraftEditor-editorContainer']")
            writePbutton.click()
        except:
            continue
        with open("twitter_usersname.txt", "r") as file:
            lines = file.readlines()
        while lines:
            
            for i in range(15):
                writePbutton1 = driver.find_element(By.XPATH , "//div[@aria-label='Tweet text']")
                writePbutton1.send_keys(lines[0])
                time.sleep(1)
                lines.pop(0)
            with open("twitter_usersname.txt", "w") as file:
                file.writelines(lines)
            writePbutton1.send_keys("منتظرين ارائكم")
            reply_button = driver.find_element(By.XPATH, "//span[text()='Reply']")
            reply_button.click()
            time.sleep(60)


                


mention()
