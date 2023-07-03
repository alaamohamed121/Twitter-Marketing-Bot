from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# Initialize the Chrome browser
link = input("link:")
driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://twitter.com/")
user_choose = input("Do u scrape tweet likes(1) or retweet(2) or followers(3):")


def likes():
    
    link= link +"/likes"
    driver.get(link)
    time.sleep(2)

    skip = input("continue:")
    while True:
        choice = input("Enter 1 to extract users, or any other key to exit: ")
        if choice == "1":
            
            users = driver.find_elements(By.XPATH ,"//a[@class='css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1wbh5a2 r-dnmrzs r-1ny4l3l']")
            with open("twitter_usersname.txt", "a") as f:
                for i in users:
                    href = i.get_attribute("href")
                    username = href.split("twitter.com/")[1]
                    f.write("@" +username + "\n")

            # Open the input file for reading
            with open("twitter_usersname.txt", "r") as f:
                # Read the file contents into a list
                lines = f.readlines()

            # Remove duplicates from the list
            unique_lines = list(set(lines))

            # Open the output file for writing
            with open("twitter_usersname.txt", "w") as f:
                # Write the unique lines to the output file
                f.writelines(unique_lines)
        else:
            break
            driver.quit()
            


def retweet():
    link = input("link:")
    link= link +"/retweets"
    driver.get(link)
    time.sleep(2)

    skip = input("continue:")
    while True:
        choice = input("Enter 1 to extract users, or any other key to exit: ")
        if choice == "1":
            
            users = driver.find_elements(By.XPATH ,"//a[@class='css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1wbh5a2 r-dnmrzs r-1ny4l3l']")
            with open("twitter_usersname.txt", "a") as f:
                for i in users:
                    href = i.get_attribute("href")
                    username = href.split("twitter.com/")[1]
                    f.write("@" +username + "\n")

            # Open the input file for reading
            with open("twitter_usersname.txt", "r") as f:
                # Read the file contents into a list
                lines = f.readlines()

            # Remove duplicates from the list
            unique_lines = list(set(lines))

            # Open the output file for writing
            with open("twitter_usersname.txt", "w") as f:
                # Write the unique lines to the output file
                f.writelines(unique_lines)
        else:
            break
            driver.quit()
            

def followers():
    link = input("link:")
    link= link +"/followers"
    driver.get(link)
    time.sleep(2)

    skip = input("continue:")
    while True:
        choice = input("Enter 1 to extract users, or any other key to exit: ")
        if choice == "1":

            users = driver.find_elements(By.XPATH ,"//a[@class='css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1wbh5a2 r-dnmrzs r-1ny4l3l']")
            with open("twitter_usersname.txt", "a") as f:
                for i in users:
                    href = i.get_attribute("href")
                    username = href.split("twitter.com/")[1]
                    f.write("@" +username + "\n")

            # Open the input file for reading
            with open("twitter_usersname.txt", "r") as f:
                # Read the file contents into a list
                lines = f.readlines()

            # Remove duplicates from the list
            unique_lines = list(set(lines))

            # Open the output file for writing
            with open("twitter_usersname.txt", "w") as f:
                # Write the unique lines to the output file
                f.writelines(unique_lines)
        else:
            break
            driver.quit()


if user_choose == "1":
    likes()
elif user_choose == "2":
    retweet()
elif user_choose == "3":
    followers()
    
else:
    print("wrong choise")
