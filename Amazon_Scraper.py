import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import random

product=input("Enter a product you want:")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

url=(f"https://www.amazon.in/s?k={product}")
response=requests.get(url,headers=headers)

soup=BeautifulSoup(response.text,"html.parser")

Product_List=[]

for item in soup.select('div.s-main-slot div.s-result-item'):
    Name_tag=item.select_one("h2 span")
    Price_tag=item.select_one("span.a-price-whole")
    if Name_tag and Price_tag:
        Name=Name_tag.get_text(strip=True)
        Price=Price_tag.get_text(strip=True).replace(",","")
        Product_List.append({
            "Product_name":Name,
            "Price (INR)":Price
        })


df=pd.DataFrame(Product_List)
df.to_csv("Amazon_Products.csv",index=False)
print("Data saved to 'Amazon_Products.csv' file")
    
