from selenium import webdriver
from selenium.webriver.common.by import BY
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scrape_data = []
def scrape():
    soup = BeautifulSoup(browser.page_source,"html.parser")
    bright_star_table = soup.find("table",attrs = {"class","wikitable"})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all('td')
        temp_list = []
        for columns_data in table_cols:
            data = columns_data.text.strip()
            temp_list.append("data")

    scrape_data.append(temp_list)

scrape()
stars_data = []
for i in range(0,len(scrape_data)):
    star_names = scrape_data[i][1]
    distance = scrape_data[i][3]
    mass = scrape_data[i][5]
    radius = scrape_data[i][6]
    lum = scrape_data[i][7]
    require_data = [star_names,distance,mass,radius,lum]
    stars_data.append(require_data)

headers = ['star_name','distance','mass','radius','luminosity']
star_df_1 = pd.DataFrame(stars_data,columns = headers)
star_df_1.to_csv('scrape_data.csv',index = True,index_label = "id")    
