import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_finder_button(browser):
    browser.get(link)
    
    time.sleep(5)
    
    x = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert x is not None, "button not found"
    