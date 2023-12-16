# SMTP simple mail transfer protocol
import smtplib
import datetime as dt
import random

MY_EMAIL = "rkrakhichoudhary@gmail.com"
MY_PASSWORD = "cdcz easr ghvn ugfn"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quote.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="madhavkumar60@gmail.com",
                            msg=f"Subject: Monday Motivation\n\n{quote}")


# my_email = "rkrakhichoudhary@gmail.com"
# password = "cdcz easr ghvn ugfn"
#
#


