import streamlit as st
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

st.title('Hello, Shopper! Find Everything You Need at BuySphere!!!!')
# with st.sidebar:
st.sidebar.header("Welcome")
excel_file='Amazondataset.csv'
df=pd.read_csv(excel_file,usecols=["product_name","category","actual_price","rating"])
# df=df.reset_index(drop=True)
category=df["category"].unique().tolist()
price=df["actual_price"].tolist()
t=st.sidebar.button("About")
cont=st.sidebar.button("Contact Us")
if(cont):
    st.sidebar.write("Support@buysphere.com")
fltr=st.sidebar.checkbox("Apply Filter")
if(fltr):
    ms=st.sidebar.multiselect("Enter category",category)
    ps=st.sidebar.slider('Price Range : ',value=(1,100000))
    rating=df["rating"]
    r=st.sidebar.slider("Rating : ",value=(min(rating),max(rating)))    
    b=st.sidebar.button("Apply Filter")
    if(b):
        mask=(df["category"].isin(ms)) & (df["actual_price"].between(*ps)) & (df["rating"].between(*r))
        n=df[mask]
        nd=n.shape[0]
        if(nd>10):
            nf="dema.xlsx"
            n.to_excel(nf,index=False,engine="openpyxl")
            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            send="muhunthane03@gmail.com"
            password="srda znyl lgom kbch"
            reciever="easumuhunthan@gmail.com"
            subject="Product List"
            message=MIMEMultipart()
            message["Subject"]=subject
            file=open(nf, "rb")  # Open the file in binary read mode
            attached = MIMEApplication(file.read(), _subtype='xlsx')  # Read file content
            attached.add_header('Content-Disposition', 'attachment', filename='dema.xlsx')
            message.attach(attached)

            server.login(send,password)
            server.sendmail(send,reciever,message.as_string())
            st.success("✅Check Your Mail We have Sent the List Of Products That You Have Applied!!!")
           
        elif(nd>1):
            st.write(n)

        else:
            st.error("Not Found Any Product")

if(t):
    st.header("About BuySphere")
    st.write('''Welcome to BuySphere, your one-stop destination for seamless online shopping! We bring you a wide range of products across various categories, ensuring quality, affordability, and convenience at your fingertips.

At BuySphere, we believe in:\n
✔ Diverse Selection From electronics to fashion, home essentials, and more.\n
✔ Affordable Prices Competitive deals and discounts for every budget.\n
✔ Secure Shopping Safe transactions and reliable payment options.\n
✔ Fast Delivery Timely shipping to get your products to you quickly.\n
✔ Customer Support Dedicated assistance to enhance your shopping experience.\n
Join thousands of happy shoppers and experience effortless online shopping with BuySphere today!''')