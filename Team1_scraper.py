#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
import urllib.request, urllib.error, urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import datetime


# In[9]:


price_list=[]
vol_24h=[]
c_time=[]
timestamp=[]


# In[10]:


chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('D:\Purdue Courses\Fall Mod 2\MGMT 590 Web Data Analytics\chromedriver.exe', options = chrome_options)
url="https://cryptowat.ch/"
driver.get(url)

flag=True

while flag==True:
    html = driver.page_source
    soup = bs(html, 'html.parser')

    ts=time.time()
    now = datetime.now()
    c_time.append(now.strftime("%H:%M:%S"))
    timestamp.append(ts)
    price=soup.find('a', class_="_1Zsf6CmsbWvG2llu3AaxDK GRK7-RzHPDRji9qMEqNeK pointer")
    btc_price=price.find('span', class_='price')
    price_list.append(btc_price.text)
    vol=soup.find_all('div',class_='text-right _1LsWw6Kho-9JZUlFg6H2zA _2MMQdwlpwp-u43vZS7_b7L _5cACuXpmVsfOHzxs3RPZS')
    vol_24h.append(vol[1].text)
    time.sleep(2)
driver.quit()


# In[89]:


data = pd.DataFrame(list(zip(c_time, timestamp, price_list, vol_24h)), 
               columns =['Current Time','TimeStamp', 'Price', 'Vol_24h'])


# In[94]:



data=pd.read_csv("D:\Purdue Courses\Fall Mod 2\MGMT 590 Big Data Technologies\project_data.csv", names=['Current Time', 'Price'])
data


# In[95]:


for i in range (len(data)):
    data['Current Time'][i]=datetime.datetime.strptime(data['Current Time'][i], '%Y-%m-%d %H:%M:%S')


# In[96]:


data['Price'] = data['Price'].apply(lambda r: float(r))


# In[97]:


final_grouped_data=data.groupby(pd.Grouper(key='Current Time', freq='60s'))['Price'].mean()


# In[98]:


final_grouped_data.to_csv('D:\Purdue Courses\Fall Mod 2\MGMT 590 Big Data Technologies\project_data.csv')


# In[99]:


data_process = pd.read_csv('D:\Purdue Courses\Fall Mod 2\MGMT 590 Big Data Technologies\project_data.csv', names=['Time','Price'])
data_process.head()


# In[100]:


log_price=[]
for i in range(0, len(data_process)):
    log_price.append(np.log(data_process['Price'][i]))
    
data_process['log_price']=log_price


# In[109]:


data_process['log_diff']= data_process['log_price']-data_process['log_price'].shift()
data_process.fillna(0)

for i in range(0, len(data_process)):
    data_process['Time'][i]=data_process['Time'][i][11:]


# In[115]:


data_process=data_process[['Time','log_price']]


# In[116]:


data_process.to_csv("D:\Purdue Courses\Fall Mod 2\MGMT 590 Big Data Technologies\project_data_log.txt", index=False)


# In[113]:





# In[ ]:




