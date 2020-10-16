from selenium import webdriver
import time
import os
import platform
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


def ip_change_macos():
    random.shuffle(ips)
    ip = ips[random.randrange(0, len(ips))]
    print('using', ip)
    os.system(f'networksetup -setmanual "Wi-Fi" {ip}')


def ip_change_linux():
    random.shuffle(ips)
    ip = ips[random.randrange(0, len(ips))]
    print('using', ip)
    os.system(f'ifconfig eth0 {ip} netmask 255.255.255.0 up')


def ip_change_windows():
    random.shuffle(ips)
    ip = ips[random.randrange(0, len(ips))]
    print('using', ip)
    pyautogui.typewrite('netsh interface ipv4 set address name="Wi-Fi" static ' + ip)
    pyautogui.press('enter')
    print('ip changed successfully')


try:
    link = str(input("Enter the URL of the Youtube Video: "))
    Timer = int(input("Enter the number of seconds you want: "))

    views = int(input('Enter the number of views you want: '))

    driver = webdriver.Chrome()
    driver.get(link)

    for i in range(views):
        if platform.system() == 'Darwin':
            ip_change_macos()
            print(platform.system())
        elif platform.system() == 'Windows':
            ip_change_windows()
            print(platform.system())
        elif platform.system() == 'Linux':
            ip_change_linux()
            print(platform.system())
        time.sleep(Timer)
        driver.refresh()
        print(i)
except:
    print("wrong url")
