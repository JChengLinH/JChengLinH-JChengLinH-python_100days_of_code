from lib2to3.pgen2 import driver
from selenium import webdriver
import time
selenium_path = r"C:\Development\chromedriver.exe"

driver = webdriver.Chrome(selenium_path)
driver.get("https://www.amazon.com/")
time.sleep(100)