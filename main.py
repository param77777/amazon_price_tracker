from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import requests
import smtplib

load_dotenv()

my_mail = os.getenv("MY_EMAIl")
my_password = os.getenv("MY_PASSWORD")

practice_url = "https://appbrewery.github.io/instant_pot/"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

response = requests.get(url=practice_url, headers=header)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")

price = soup.find(class_ = "a-offscreen").get_text()

price_without_currency = price.split("$")[1]

slpit_price = float(price_without_currency)

buy_price = 100

subject = "Price Alert: Item is below $100!"
body = f"The current price is ${slpit_price:.2f}. Check it out here: {practice_url}"
msg = f"Subject: {subject}\n\n{body}"

if slpit_price < buy_price:
    with smtplib.SMTP("smtp.gmail.com", 587) as mail:
        mail.starttls()
        mail.login(user=my_mail, password=my_password)
        mail.sendmail(from_addr=my_mail,
                      to_addrs=my_mail,
                      msg= msg)