import smtplib
import datetime as dt
from random import choice

MY_EMAIL = "email"
MY_PASSWORD = "password"

now = dt.datetime.now()
weekday = now.weekday()
time = now.time()
hour = time.hour

list_of_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if hour == 8:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="email@gmail.com",
            msg=f"Subject:{list_of_days[weekday]} Motivation\n\n{quote}"
        )
