from email.mime.text import MIMEText
import smtplib
import datetime as dt
from random import choice

MY_EMAIL = "email"
MY_PASSWORD = "password"
RECIPIENTS = ["firstperson@gmail.com", "secondperson@yahoo.com", "thirdperson@gmail.com", "fourthperson@gmail.com"]

now = dt.datetime.now()
weekday = now.weekday()
time = now.time()
hour = time.hour

list_of_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = choice(all_quotes)

if hour == 8:
    for email in RECIPIENTS:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)

            msg = MIMEText(f"{quote}")
            msg["Subject"] = f"{list_of_days[weekday]} Motivation"
            msg["From"] = MY_EMAIL
            msg["To"] = email
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=msg.as_string()
            )
