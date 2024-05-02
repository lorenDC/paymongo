from getgauge.python import before_suite, before_spec, before_step, data_store
from datetime import datetime
now = datetime.now()
from colorama import Fore
import getpass
import os
# DATA MANIPULATION
import pandas as pd # data processing
import numpy as np
from pandas import ExcelWriter
import json as json
import openpyxl

@before_suite
def get_username():return getpass.getuser()
def get_datetime(now):return now.strftime("%d %b, %Y | %I:%M %p")
data_store.suite.UserInfo = (get_datetime(now),get_username())
print('\x1b[1;31m'+Fore.CYAN + data_store.suite.UserInfo[0]+'\x1b[0m')
print('\x1b[1;31m'+Fore.CYAN + data_store.suite.UserInfo[1]+'\x1b[0m')

# Database Connections
@before_suite
def connection(context):
    data_store.suite.user = data_store.suite.UserInfo[1].casefold()
    username = data_store.suite.user+'@gmail.com'

    #ScoreUI URL
    data_store.suite.htmlURL = "https://dashboard.uat.paymongo.dev/signup"

@before_suite
def read_data(context):
    # Create input path variable for Test Data
    os.chdir('C:/Users/'+data_store.suite.user+'/OneDrive/Documents/github/gauge_paymongo/gauge-paymongo/step_impl/inputs')
    data_store.suite.Path = 'C:/Users/'+data_store.suite.user+'/OneDrive/Documents/github/gauge_paymongo/gauge-paymongo/reports/html-report/screenshots'

    data_store.suite.filename = 'Paymongo Harness v1.xlsx'
    data_store.suite.resultfile = ('screenshots_{}.png'.format(now.strftime("%d%m%Y%I%M%S")))

    print(Fore.BLUE +'FilePath: {}'.format(data_store.suite.Path))

    data_store.suite.positive = "Positive"
    data_store.suite.negative = "Negative"

    data_store.suite.dtypes = {'VehicleID':str, 'TransactionTimeStamp':str, 'Target PriceIndex':str,'Mobile number':str}

# %%time
@before_spec
def dataset(context):
# Read Test dataset
    print ('Reading Data...')
    xls = pd.ExcelFile(data_store.suite.filename)
    data_store.spec.tdata = pd.read_excel(xls,sheet_name = data_store.suite.positive,skiprows=1,dtype=data_store.suite.dtypes,na_values=[''])
    data_store.spec.err = pd.read_excel(xls,sheet_name = data_store.suite.negative,skiprows=1,dtype=data_store.suite.dtypes,na_values=[''])

    #fill out the missing values
    data_store.spec.tdata=data_store.spec.tdata.fillna('')
    data_store.spec.err=data_store.spec.err.fillna('')

    print ('Done Reading Data')