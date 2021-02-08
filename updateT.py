from selenium import webdriver
import time
import getpass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import csv

from datetime import datetime
import bot
import tbot

def updatebot():
    options = webdriver.ChromeOptions()
    options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    chrome_driver_binary = "chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver_binary, options=options)


    # driver = webdriver.Chrome()
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 1080)

    # opening the website using get()
    driver.get('https://www.pythonanywhere.com/')

    login = driver.find_element_by_class_name('login_link')
    login.click()

    # setting user inputs to the portal
    # username
    username = driver.find_element_by_id('id_auth-username')
    username.send_keys("USERNAME")

    #password
    password = driver.find_element_by_id('id_auth-password')
    password.send_keys("PASSWORD")

    # clicking login button
    submit = driver.find_element_by_id('id_next')
    submit.click()

    # wait time for the site to load
    # driver.implicitly_wait(30)
    # myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="form1"]/div[3]/section[2]/div/div/div[1]/h5')))

    # clicking and opening glearn sitye
    browse_files = driver.find_element_by_xpath("/html/body/div[1]/main/div/div[3]/div/div[2]/div/div/a")
    browse_files.click()

    gmeetings = driver.find_element_by_xpath('//*[@id="id_row_directory_4"]/td[1]/a')
    gmeetings.click()

    # meetcsv = driver.find_element_by_xpath('//*[@id="id_row_file_1"]/td[1]/div/a')
    # meetcsv.click()

    upload = driver.find_element_by_xpath('//*[@id="id_upload_filename"]')
    # upload.click()
    upload.send_keys("G://Hari/github-cloud/GITAM-AutoLogin/meet.csv")

