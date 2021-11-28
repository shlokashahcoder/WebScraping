from selenium import webdriver 
from bs4 import BeautifulSoup 
import time 
import csv

start_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser = webdriver.Chrome("C:/Users/Admin/Desktop/Python/Planet Application/web scraping/chromedriver.exe") 
browser.get(start_url) 
time.sleep(10)

def getData():
    headers =["NAME","LIGHT-YEARS FROM EARTH","PLANET MASS","STELLAR MAGNITUDE","DISCOVERY DATE"]
    planets_Data = []
    for i in range(0,4):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ulData in soup.find_all("ul",attrs={"class","exoplanet"}):
            liData= ulData.find_all("li")
            tempList = []
            for index, eachData in enumerate(liData):
                if index==0:
                    tempList.append(eachData.find_all("a")[0].contents[0])
                else :
                    tempList.append(eachData.contents[0])

            planets_Data.append(tempList)

    with open("scrapper_2.csv", "w") as f: 
        csvwriter = csv.writer(f) 
        csvwriter.writerow(headers) 
        csvwriter.writerows(planets_Data)

getData()

