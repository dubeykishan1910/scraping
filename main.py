
# os.environ['PATH'] += r"C:/websc"
# driver = webdriver.Chrome()

#
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.common.keys import Keys
#
# path="C:/websc/chromedriver.exe"
# s=Service(path)
# driver=webdriver.Chrome(service=s)
#
#
# #open web page in that google
# url="https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar"
# driver.get(url)
# driver.maximize_window()
#
# input_search=driver.find_element(By.ID,"twotabsearchtextbox")
# search_button= driver.find_element(By.XPATH,"//input[@type='submit']")
#
# # box=driver.find_elements_by_xpath("//*[@id='input']")
# input_search.send_keys('smartphones under 10000')
# sleep(1)
# search_button.click()
# # box.send_keys(Keys.ENTER)






from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


#Request page source from URL
url="https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar"
r=requests.get(url)
print(r)



#Read data from web-side
soup = bs(r.text, "lxml")


#soup data from perticular area of the full page
box = soup.find("span", class_="rush-component s-latency-cf-section")



#Scrap Product name,prices,reviews.

Product_name = []
Prices = []
Reviews = []


#It will create list of all Product name with Tages
names = box.find_all("span", class_="a-size-base-plus a-color-base a-text-normal")

#product prices
prices = box.find_all("span", class_="a-price-whole")

#product reviews
reviews = box.find_all("span", class_="a-icon-alt")


while (True):
    for i in range(len(names)):
        name = names[i].text
        Product_name.append(name)

        name2 = prices[i].text
        Prices.append(name2)

        name3 = reviews[i].text
        name3d = name3[:3]
        Reviews.append(name3d)

    break


df=pd.DataFrame({"Product Name":Product_name,"Prices":Prices,"Rating":Reviews})
print(df)
df.to_csv("Amazon.csv",index=False)


























