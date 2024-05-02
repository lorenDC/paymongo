from sqlalchemy import create_engine, text
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os
from step_impl.hooks import *
from getgauge.python import data_store
from datetime import datetime
now = datetime.now()
import pyautogui

def wait_until_located(parent,selector_type, value:str, timeout:int):
    element = None
    if selector_type == 'ID':
        element = WebDriverWait(parent, timeout).until(ec.presence_of_element_located((By.ID, value)))
    elif selector_type == 'XPATH':
        element = WebDriverWait(parent, timeout).until(ec.presence_of_element_located((By.XPATH, value)))
    elif selector_type == 'CLASS_NAME':
        element = WebDriverWait(parent, timeout).until(ec.presence_of_element_located((By.CLASS_NAME, value)))
    elif selector_type == 'CSS_SELECTOR':
        element = WebDriverWait(parent, timeout).until(ec.presence_of_element_located((By.CSS_SELECTOR, value)))
    else:
        print("Specify a valid parameter")

    if element:
        parent.execute_script("arguments[0].scrollIntoView();", element)

    return element

#-------ReadValues
def readValueById(parent,webElement:str):
    element = None
    element =  wait_until_located(parent,'ID', webElement, 10).text
    return element

def readValueByXpath(parent,webElement:str):
    element = None
    element =  wait_until_located(parent,'XPATH', webElement, 10).text
    return element

def readValueByClassName(parent,webElement:str):
    element = None
    element =  wait_until_located(parent,'CLASS_NAME', webElement, 10).text
    return element

def readValueByCSS(parent,webElement:str):
    element = None
    element =  wait_until_located(parent,'CSS_SELECTOR', webElement, 10).text
    return element

#-------SendValue

def sendValueById(parent,webElement:str, input_text:str):
    element = None
    element =  wait_until_located(parent,'ID', webElement, 10)
    element.send_keys(input_text)
    return element.text

def sendValueByXpath(parent,webElement:str, input_text:str):
    element = None
    element =  wait_until_located(parent,'XPATH', webElement, 10)
    element.send_keys(input_text)
    return element.text

def sendValueByClassName(parent,webElement:str, input_text:str):
    element = None
    element =  wait_until_located(parent,'CLASS_NAME', webElement, 10)
    element.send_keys(input_text)
    return element.text

def sendValueByCSS(parent,webElement:str, input_text:str):
    element = None
    element =  wait_until_located(parent,'CSS_SELECTOR', webElement, 10)
    element.send_keys(input_text)
    return element.text

#-------SelectValue

def clickValueById(parent,webElement:str):
    element = None
    element =  wait_until_located(parent,'ID', webElement, 10)
    element.click()
    return element

def clickValueByXpath(parent,webElement:str):
    element = None
    element =  wait_until_located(parent,'XPATH', webElement, 10)
    element.click()
    return element

def clickValueByClassName(parent,webElement:str):
    element = None
    element =  wait_until_located(parent,'CLASS_NAME', webElement, 10)
    element.click()
    return element

def clickValueByCSS(parent,webElement:str):
    element = None
    element =  wait_until_located(parent,'CSS_SELECTOR', webElement, 10)
    element.click()
    return element

#------Annotation
def take_screenshot():
    
    filepath = os.path.join(data_store.suite.Path, data_store.suite.resultfile)
    pyautogui.screenshot(filepath)
    print(f"Screenshot taken and saved at: {filepath}")
