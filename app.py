import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
st.set_page_config(page_title="webscaring",page_icon=":tada:",layout="wide")

st.subheader("Hi, welcome to the world of data :wave:" )
st.title("flipkart Data scraping")
st.write("I am passionate about finding the data from many web pages which gives me free data ")

name = []
Spec = []
Ratings=[]
Delivery = []
Discount =[]
Price = []
LINK = []

URL =st.sidebar.text_input("enter your URL : ")
number_of_page = st.sidebar.text_input("enter the page number:")
bt=st.sidebar.button("goo")
if bt == True:
    for i in range(1,int(number_of_page)+1):
        data =  URL+"&page="+str(i)
        req = requests.get(data)
        soup = BeautifulSoup(req.text, 'html.parser')
        Name = soup.find_all("div", {"class": "_4rR01T"})
        spec = soup.find_all("div", {"class": "fMghEO"})
        ratings = soup.find_all("div", {"class": "_3LWZlK"})
        delivery = soup.find_all("div", {"class": "_3tcB5a p8ucoS"})
        discount = soup.find_all("div", {"class": "_3Ay6Sb"})
        PRICE = soup.find_all("div", {"class": "_30jeq3 _1_WHN1"})
        Link = soup.find_all("div", {"class": "href"})


        for i in Name:
            name.append(i.text)
        for i in spec:
            Spec.append(i.text)
        for i in ratings:
            Ratings.append(i.text)
        for i in delivery:
            Delivery.append(i.text)
        for i in discount:
            Discount.append(i.text)
        for i in PRICE:
            Price.append(i.text)
        for i in Link:
            LINK.append(i.text)

data ={"name" :name,"specifications": Spec,"Ratings":Ratings,"Delivery":Delivery,"Discount":Discount,"Price":Price,"Link":LINK}
df = pd.DataFrame.from_dict(data, orient='index')
df2 = df.transpose()

df2['name'] = df2['name'].replace('-', np.nan)
df2 = df2.dropna(axis=0, subset=['name'])

df2["name"].dropna(inplace =True)
df2["Discount"].fillna("na",inplace = True)
df2["Delivery"].fillna("pay_delivery",inplace = True)


bt=st.sidebar.button("download csv file")
if bt == True:
    df2.to_csv("practo.csv")

st.dataframe(df2)

