# instagram-auto-report
# dev by: m. duong
# date: 2025-06-17
# x (twiiter) ver: coming soon :D

from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
import time


# automates instagram login and reporting
def login_report(user,pwd):
    browser = webdriver.Chrome()
    browser.get("https://instagram.com/")
    time.sleep(4)

    # login
    username = browser.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
    password = browser.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
    username.send_keys(user)
    password.send_keys(pwd)
    login_button = browser.find_element(By.XPATH,"//button//div[text()='Log in']/..")
    login_button.click()
    time.sleep(8)
    
    # read report list and report
    with open('report.txt','r') as report_file:
        report_link = report_file.readlines()
        for link in report_link:
            link = link.strip()
            if link:
                try:
                    # navigate to acc
                    browser.get(link)
                    time.sleep(3)

                    # click options
                    more_options = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[3]/div")
                    more_options.click()
                    time.sleep(2)

                    # reporting process
                    option = browser.find_element(By.XPATH,"//button[contains(text(),'Report')]")
                    option.click()
                    time.sleep(2)

                    report_option = browser.find_element(By.XPATH,"//button[.//div/div[text()='Report Account']]")
                    report_option.click()
                    time.sleep(2)

                    report_reason_1 = browser.find_element(By.XPATH,"//button[.//div[contains(text(),\"It's posting content that shouldn't be on Instagram\")]]")
                    report_reason_1.click()
                    time.sleep(2)

                    report_reason_2 = browser.find_element(By.XPATH,"//button[.//div/div[text()='Violence, hate or exploitation']]")
                    report_reason_2.click()
                    time.sleep(2)

                    report_reason_3 = browser.find_element(By.XPATH,"//button[.//div/div[text()='Hate speech or symbols']]")
                    report_reason_3.click()
                    time.sleep(2)

                    complete_button = browser.find_element(By.XPATH,"//button[contains(text(),'Close')]")
                    complete_button.click()
                    time.sleep(2)

                # if broken link or error occurs, move to next
                except Exception as e:
                    continue
    browser.quit()

# read login credentials
with open('login.txt','r') as login_file:
    lines = login_file.readlines()
    acc = []
    for i in range(0,len(lines),2):
        user = lines[i].strip()
        pwd = lines[i+1].strip()
        acc.append((user,pwd))

# threads for each acc
threads = []
for user,pwd in acc:
    t = threading.Thread(target=login_report,args=(user,pwd))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
