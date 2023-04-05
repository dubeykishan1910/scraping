
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


























