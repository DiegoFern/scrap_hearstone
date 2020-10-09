from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
import re
from pprint import pprint
import random

if not os.path.isfile('cards.txt'):
    driver = webdriver.Chrome( )
    driver.get("https://playhearthstone.com/es-es/cards")
    driver.maximize_window()
    time.sleep(1)
    #We make a slow scroll to the end of the page
    iter=1
    while True:
            scrollHeight = driver.execute_script("return document.documentElement.scrollHeight")
            Height=250*iter
            driver.execute_script("window.scrollTo(0, " + str(Height) + ");")
            if Height > scrollHeight:
                print('End of page')
                break
            time.sleep(0.3)
            iter+=1
    #we get the internal html code of the body
    body = driver.execute_script("return document.body")
    source = body.get_attribute('innerHTML')
    file = open('cards.txt','w')
    #we iterate through the different albums with beautifulsoup and load the data into the flat file
    soup = BeautifulSoup(source, "html.parser")
    for card in soup.find_all("a", class_="ksfKYw"):

        link = card['href']



        file.write(link+'\n')
    #finally we close the file and the driver
    file.close()

driver = webdriver.Chrome( )
out =[]
fileOut = open('data.txt','w')
for i in list(open('cards.txt','r'))[:]:
    driver.get("https://playhearthstone.com/es-es" + i)
    time.sleep(1)
    body = driver.execute_script("return document.body")

    source = body.get_attribute('innerHTML')
    soup = BeautifulSoup(source, "html.parser")
    title = soup.find_all("h3",class_='bwAgtA')[0].text
    ans = {

        'img':soup.find_all("img",alt=title,class_='CardImage loaded'.split())[0].attrs['src'],
        'title': title,
        'descripcion':soup.find_all("p",class_='ijEQkD')[0].text,
        'data':soup.find_all("p",class_='CardDetailsLayout__CardText-sc-4r6wq5-5 fNQbVa')[0].text,
        'li':list(map(lambda x:x.text.split('\xa0:'),
                      soup.find_all("ul",class_='CardDetailsLayout__AttributesList-sc-4r6wq5-6 exPYBL')[0].find_all('li'),

                    )
                  )
        }

    print(ans,file=fileOut)
    out.append(ans)
