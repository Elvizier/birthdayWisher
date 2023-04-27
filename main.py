print("+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+")
print("|A|U|T|O|M|A|T|I|C| |H|A|P|P|Y| |B|I|R|T|H|D|A|Y| |W|I|S|H|E|R|")
print("+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+")

print("Welcome to Automatic Happy Birthday Wisher")
print("Please Add your contacts to the birthdays.csv File")

import pandas as pd, random, smtplib, datetime as dt

now = dt.datetime.now() #To get the current date
day = now.day
month = now.month

# sender email account
my_email = input("Please enter your email : ")
password = input("Enter email password (Check with your provider on how to get app access password) : ")
smtp =  input("Email provider SMTP : ")
# get data using pandas 
data = pd.read_csv("birthdays.csv")


# Dictionary templates for panda Dataframe
birthdays_dict = data.set_index('name')[['email', 'month', 'day']].to_dict('index')


#Loop through the dictionary and check if month and day matches today
for name, info in birthdays_dict.items():
    if info["month"] == month and info["day"] == day:
        rn = random.randint(1, 3) 
        with open(f"letter_templates/letter_{rn}.txt", "r") as file:
            letter_content = file.read()
            #replacing the name in the letter to the matching name
            personalized_letter = letter_content.replace("[NAME]", name)
        with smtplib.SMTP(smtp) as connection:
            # Encrypt our message
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=info["email"], 
                msg=f"Subject:Happy Birthday\n\n{personalized_letter}"
            )

print("Birthday emails processed successfully!")