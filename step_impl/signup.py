#System 
import sys,os
import time
from datetime import datetime
now = datetime.now()
import warnings
warnings.filterwarnings("ignore")
from colorama import Fore

# DATA MANIPULATION
import pandas as pd # data processing
import numpy as np
from pandas import ExcelWriter

#Selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from getgauge.python import data_store, step, continue_on_failure

from step_impl.hooks import *
from step_impl.ui_functios import *

#Choose browser
@step("Choose browser <browserflag>")
def environment_params(browserflag):
    data_store.scenario.browser = browserflag

@continue_on_failure([])
@step("Run Positive Harness")
def test_functions():

    # for i in data_store.spec.tdata.index:
    for i in range (0,1):
        print(i, end='; ')

        inpBusinessName = (data_store.spec.tdata['Business name'][i])
        inpFirstName = (data_store.spec.tdata['First name'][i])
        inpLastName = (data_store.spec.tdata['Last name'][i])
        inpMobileNum = (data_store.spec.tdata['Mobile number'][i])
        inpEmailAdd = (data_store.spec.tdata['Email address'][i])
        inpPassword = (data_store.spec.tdata['Password'][i])

        inpAvgRevenue = (data_store.spec.tdata['Average revenue'][i])

        if inpAvgRevenue == "< 100K":
            inpAvgRev = '//*[@id="root"]/section/div/div[1]/div[12]/ul/li[1]/button/div'
        elif inpAvgRevenue == "100K - 300K":
            inpAvgRev = '//*[@id="root"]/section/div/div[1]/div[12]/ul/li[2]/button/div'
        elif inpAvgRevenue == "300K - 500K":
            inpAvgRev = '//*[@id="root"]/section/div/div[1]/div[12]/ul/li[3]/button/div'
        elif inpAvgRevenue == "500K - 1M":
            inpAvgRev = '//*[@id="root"]/section/div/div[1]/div[12]/ul/li[4]/button/div'
        elif inpAvgRevenue == "1M - 3M":
            inpAvgRev = '//*[@id="root"]/section/div/div[1]/div[12]/ul/li[5]/button/div'
        elif inpAvgRevenue == "> 3M":
            inpAvgRev = '//*[@id="root"]/section/div/div[1]/div[12]/ul/li[6]/button/div'
        else:
            print('Please select Average Revenue')

        inpIntention = (data_store.spec.tdata['Intention'][i])

        if inpIntention == "None yet. I am still learning about PayMongo":
            inpInt = '//*[@id="root"]/section/div/div[1]/div[14]/ul/li[1]/button/div'
        elif inpIntention == "I don't have a registered business. I inted to use PayMongo for personal use":
            inpInt = '//*[@id="root"]/section/div/div[1]/div[14]/ul/li[2]/button/div'
        elif inpIntention == "I'm signing up for test purposes":
            inpInt = '//*[@id="root"]/section/div/div[1]/div[14]/ul/li[3]/button/div'
        elif inpIntention == "I plan to start a business soon":
            inpInt = '//*[@id="root"]/section/div/div[1]/div[14]/ul/li[4]/button/div'
        elif inpIntention == "I want to apply for a business loan":
            inpInt = '//*[@id="root"]/section/div/div[1]/div[14]/ul/li[5]/button/div'
        elif inpIntention == "I want to apply personal loan":
            inpInt = '//*[@id="root"]/section/div/div[1]/div[14]/ul/li[6]/button/div'
        elif inpIntention == "I want to integrate it with my website or mobile app":
            inpInt = '//*[@id="root"]/section/div/div[1]/div[14]/ul/li[7]/button/div'
        elif inpIntention == "I want to send money for my business expenses":
            inpInt = '//*[@id="root"]/section/div/div[1]/div[14]/ul/li[8]/button/div'
        elif inpIntention == "I want one-time payment links":
            inpInt = '//*[@id="root"]/section/div/div[1]/div[14]/ul/li[9]/button/div'
        elif inpIntention == "I want to have reusable checkout page":
            inpInt = '//*[@id="root"]/section/div/div[1]/div[14]/ul/li[10]/button/div'
        elif inpIntention == "I want to accept payments with my e-commerce platforms (Shopify, WooComm, etc.)":
            inpInt = '//*[@id="root"]/section/div/div[1]/div[14]/ul/li[11]/button/div'
        else:
            print('Please select Intention')
            print(inpInt)
        
        # inpReferralCode = (data_store.spec.tdata['Referral Code'][i])

        try:

            #HTML Resquest
            response_url = data_store.suite.htmlURL
            # htmlUrlList.append(response_url)

            if (data_store.scenario.browser =="edge"):
                options = webdriver.EdgeOptions()
                # options.headless = True
                driver = webdriver.Edge(options=options)
            else:
                options = webdriver.ChromeOptions()
                # options.headless = True
                options.add_argument('--no-sandbox')
                driver = webdriver.Chrome(options=options)
            
            htmlurl =  response_url   
            driver.get(htmlurl)
            driver.maximize_window()
            
            time.sleep(5)

            #------Input Dashboard

            sendBusinessName = sendValueById(driver,'businessName',inpBusinessName)
            sendFirstName = sendValueById(driver,'firstName',inpFirstName)
            sendLastName = sendValueById(driver,'lastName',inpLastName)
            sendMobileNum = sendValueById(driver,'contactNumber',inpMobileNum)
            sendEmailAdd = sendValueById(driver,'email',inpEmailAdd)
            sendPassword = sendValueById(driver,'password',inpPassword)

            avgRevenue = '//*[@id="root"]/section/div/div[1]/div[12]/button/div[1]'
            clickValueByXpath(driver,avgRevenue)
            if clickValueByXpath(driver,avgRevenue):
                selectRevenue = clickValueByXpath(driver,inpAvgRev)
    
            intention = '//*[@id="root"]/section/div/div[1]/div[14]/button/div[2]'
            
            clickValueByXpath(driver,intention)
            clickValueByXpath(driver,inpInt)
            # if clickValueByXpath(driver,intention):
            #     selectIntention = clickValueByXpath(driver,'//*[@id="root"]/section/div/div[1]/div[14]/ul/li[1]/button/div')      
        
            # if data_store.spec.tdata['Referral Code'] != '':
            #     addReferral = '//*[@id="root"]/section/div/div[1]/div[15]/div/a/span'
            #     inpRefCode = '//*[@id="refrerralCode"]'
            #     clickValueByXpath(driver,addReferral)
            #     if clickValueByXpath(driver,inpRefCode):
            #         sendRefCode = sendValueById(driver,'referralCode',inpReferralCode)
            # else:
            clickValueById(driver,'acceptedTerms')
            clickValueByXpath(driver,'//*[@id="root"]/section/div/div[1]/button/div')  
            time.sleep(5)
            take_screenshot() 

        except KeyError as e:
            driver.close(); driver.quit()
            continue