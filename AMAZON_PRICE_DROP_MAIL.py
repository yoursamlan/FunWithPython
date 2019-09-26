import requests,os,sys,time
from bs4 import  BeautifulSoup
import smtplib

url = input("Enter your URL here : ")
dp = int(input("Enter your desired price : "))
'''
url = "https://www.amazon.in/Philips-Trimmer-Cordless-QT4001-15/dp/B00L8PEEAI/ref=sr_1_4?crid=26OVQAIRQLJUU&keywords=philips+qt4011%2F15&qid=1569507835&s=hpc&sprefix=philips+qt%2Chpc%2C361&sr=1-4"
dp = 1000
'''
URL = url
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}


page = requests.get(URL, headers=headers)

soup= BeautifulSoup(page.content,'html.parser')

'''
m=open('soupw.txt',"wb")
m.write(soup.prettify().encode("utf-8"))
m.close
'''

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
main_price = price[2:]

#--------MAKE IT AN INTEGER------------
l = len(main_price)
if l<=6 :
    main_price = price[2:5]
else:
    p1 =  price[2]
    p2 =  price[4:7]
    pf = str(p1)+str(p2)
    main_price = int(pf)
    
price_now = int(main_price)

title1=str(title.strip())
main_price1 = main_price
print(title1)
print(main_price1)
#------------------------------------------Temporary fixed for values under Rs. 9,999

'''
print(title.strip())
print(price.strip())
print(main_price)

print(real_price)
print(type(real_price))
print(dp)
print(type(dp))
'''
#FUNCTION TO CHECK PRICE____________________________________________________


def check_price():
    if(price_now <= dp):
        send_mail()
        


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('dev.amlan.99@gmail.com','gzanpwfvxnldiycw')

    subject = "Price of "+title1+" has fallen down to Rs. "+str(main_price1)
    body = "Hey Amlan! \n Price of "+title1+" has fallen down to Rs. "+str(main_price1)+", which is less than your desired price of Rs."+str(dp)+" .\n So, hurry up and check the amazon link right now : "+url

    msg = f"Subject: {subject} \n\n {body} "

    server.sendmail(
        'dev.amlan.99@gmail.com',
        'amlan99@tutanota.com',
        msg
    )
    print("HEY AMLAN, EMAIL HAS BEEN SENT SUCCESSFULLY.")

    server.quit()
    
while(True):
    check_price()
    time.sleep(3600)

#(On windows 10. Haven't tested on other versions of windows or any other os) Make the .py file .pyw file. Then type win+r and type 'shell:startup'. It will open a folder where you move your .pyw file or shortcut to it. Next time you boot it will run script silently on the background. You're welcome.'''

    
    
    

        
