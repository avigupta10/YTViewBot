from selenium import webdriver
import time

link = str(input("Enter the URL of the Youtube Video: "))
Timer = int(input("Enter the time delay you want: "))

views = int(input('Enter the number of views you want: '))

driver = webdriver.Chrome()
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
    print(i)
    exit()

