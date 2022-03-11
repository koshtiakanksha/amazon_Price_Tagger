import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

MY_EMAIL = "yours"
MY_PASSWORD = "yours"

URL = "https://www.amazon.in/Dell-Km117-Wireless-Keyboard-Mouse/dp/B01LOORNLY?ref_=Oct_d_obs_d_1375418" \
      "031&pd_rd_w=wR8d8&pf_rd_p=6a6b213b-2f3b-4413-8099-742b8c9f52a9&pf_rd_r=GBH11D4543BH4Q0S1SXY&pd_rd_r=19ac19c3-c" \
      "02a-404d-8ad1-c56bd79f1735&pd_rd_wg=MNycY&pd_rd_i=B01LOORNLY"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "yours"
}
response = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(response.content, "lxml")

price = float(soup.find(class_="a-price-whole").get_text().split(",")[0] +
              soup.find(class_="a-price-whole").get_text().split(",")[1])

if price<1400:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="******@gmail.com",
            msg=f"Subject:Price Drop Alert\n\nHey! The price of the product that you wanted from Amazon has "
                f"dropped to a number you can afford! Bag it before the price rises again!"
        )
