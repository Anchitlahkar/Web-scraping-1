import pandas as pd
import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome(
    "D:/System install files/chromedriver_win32/chromedriver")

browser.get(START_URL)

time.sleep(5)

temp_star_data = []
star_data = []

headers = ["name", "distance", "mass", "radius"]




Soup = BeautifulSoup(browser.page_source, "html.parser")

temp_list = []
for tr_tags in Soup.find_all('tr'):
    
    td = tr_tags.find_all("td")
    rows = [i.text.rstrip() for i in td]
    temp_list.append(rows)


name = []
distance = []
mass = []
radius = []

for i in range(1,len(temp_list)):

    name.append(temp_list[i][1])
    distance.append(temp_list[i][3]) 
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6]) 

os.system("CLS")

rows = pd.DataFrame(list(zip(name, distance, mass, radius )),columns=['Star_name','Distance','Mass','Radius'])

rows.to_csv('star_data.csv')