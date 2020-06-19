import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = 'PRODUCT URL'


header = {'YOUR USER AGENT'}

limit = YOUR PRICE

def check_product():
    page = requests.get(url, headers=header)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="title_feature_div").get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    global price
    convert_p = price.strip()
    print("product:")
    print(title.strip())
    
    print("price:")
    print(convert_p)
    
    if price < limit:
        send_email()
    elif price == limit:
        send_email()
    else:
        continue

# send email
def send_email():
    server = smtplib.SMTP(host='smpt.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('YOUR EMAIL ID', 'YOUR EMAIL PASSWORD')

    if price == limit:
        subject = "price is equal to your price"
    else:
        subject = "prcie wnis do"

    body = f"check here {url}"

    msg = f"Subject: {subject}\n\n {body}"

    server.sendmail(
        'YOUR EMAIL ID',
        'RECEIVER"S EMAIL ID',
        msg
    )
    print("email send")


while price < limit :
    check_product()
    time.sleep(3600)
    