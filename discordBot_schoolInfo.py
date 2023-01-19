from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
import time

today = datetime.today().strftime('%Y-%m-%d').replace("-", "")
print("Date (URL format): " + today)
vahsURL = "https://www.verona.k12.wi.us/Page/28#calendar16/" + today + "/day"
print("URL used: " + vahsURL)
classToFind = "wcm-calendar-event-title"

browser = webdriver.Firefox()
browser.get(vahsURL)
print("waiting for page to load...")
time.sleep(5)
print("scrapping page...")
elements = browser.find_elements(By.CLASS_NAME, classToFind)
print("parsing info...")

evenDays = False
for element in elements:
    text = element.text
    if(text == "Periods 2, 4, 6, 7"):
        evenDays = True
browser.close()

if(evenDays):
    print("Today is an even day")
else:
    print("Today is an odd day")
exit()
