from selenium import webdriver
import time
import os
import pyautogui
import random

ips = ['192.168.1.1',
       '192.168.1.1',
       '192.168.0.1',
       '192.168.0.10',
       '192.168.0.101',
       '192.168.0.30',
       '192.168.0.50',
       '192.168.1.254',
       '192.168.15.1',
       '192.168.254.254']


def ip_change():
    random.shuffle(ips)
    ip = ips[random.randrange(0, len(ips))]
    print('using', ip)
    pyautogui.typewrite('netsh interface ipv4 set address name="Wi-Fi" static ' + ip)
    pyautogui.press('enter')
    print(f'ip successfully changed to {ip}')


link = str(input("Enter the URL of the Youtube Video: "))
Timer = int(input("Enter the number of seconds you want: "))

views = int(input('Enter the number of views you want: '))

driver = webdriver.Chrome()
driver.get(link)

for i in range(views):
    ip_change()
    time.sleep(Timer)
    driver.refresh()
    print(i)

