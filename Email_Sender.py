from email.message import EmailMessage
import ssl
import smtplib
from datetime import date, datetime
import random
import time
import pytz

times_sent = 1

#OPTIMIZE: if the hour is not between 7:00-18:00, dont let it check every minute again and again. just let it sleep.

def email_sender_to_military(times_sent, now_time): #Putting it in a function for comfort


    #EVERYTHING ORGANIZED. -unnecessary
    email_sender = "ramavni1@gmail.com" #From Email
    email_password = "jnizoewdswotfmok"
    email_reciever = "ramavni1@gmail.com" #To Email

    subject = 'וואו זה אשכרה עובד' + now_time # Title

    body = """
    מה שכתוב אשכרה במייל
    נשלח %d פעמים

    """ % times_sent


    #Setting everything in EmailMessage from the library EmailMessage
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['Subject'] = subject
    em.set_content(body) #Body content


    #SSL ENCRYPTION
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: #Server (Gmail), PORT, CONTEXT
        smtp.login(email_sender, email_password) #Connect to Gmail
        smtp.sendmail(email_sender, email_reciever, em.as_string()) #The actual sender


def current_time():
    #Current Time - Israel
    israel_time = pytz.timezone('Israel')

    #Making now Class (is it called 'class'?)
    now = datetime.now(israel_time)
    now_hour = now.strftime("%H")
    now_minute = now.strftime("%M")
    now_time = now_hour + ':' + now_minute

    return now_time

    #Randomizes a time between 8:00 - 18:00, In which it sends the message
def random_times():
    #First hour Randomizer
    ran_hour_0 = random.randint(7,18)
    ran_minute_0 = random.randint(0, 60)
    if ran_hour_0 == 18: ran_minute_0 = 0
    if int(ran_minute_0) < 10: ran_minute_0 = '0' + str(ran_minute_0)

    ran_time_0 = str(ran_hour_0) + ':' + str(ran_minute_0)

    #Second hour Randomizer
    #If 1st hour is BIGGER by 3 than 0st hour OR if 1st hour is SMALLER by 3 than 1st hour, go on.
    while True: 
        ran_hour_1 = random.randint(7,18)
        ran_minute_1 = random.randint(0, 60)
        if ran_hour_1 == 18: ran_minute_1 = 0
        if int(ran_minute_1) < 10: ran_minute_1 = '0' + str(ran_minute_1)

        if (ran_hour_1 >= ran_hour_0 + 3 or ran_hour_1 <= ran_hour_0 - 3):
            break
        else:
            continue

    ran_time_1 = str(ran_hour_1) + ':' + str(ran_minute_1)

    #Third hour Randomizer
    #If 2nd hour is BIGGER by 3 than 0st hour AND if 2nd hour is BIGGER than 1st hour, go on. Example: 0st: 8:00, 1st: 12:00, 2nd: 16:00
    #If 2nd hour is SMALLER by 3 than 0st hour AND if 2nd hour is SMALLER than 1st hour, go on.
    while True:
        ran_hour_2 = random.randint(7,18)
        ran_minute_2 = random.randint(0, 60)
        if ran_hour_2 == 18: ran_minute_2 = 0
        if int(ran_minute_2) < 10: ran_minute_2 = '0' + str(ran_minute_2)

        if ((ran_hour_2 >= ran_hour_0 + 3 and ran_hour_2 >= ran_hour_0 + 3)
        or (ran_hour_2 <= ran_hour_0 - 3 and ran_hour_2 <= ran_hour_0 - 3)):
            break
        else:
            continue

    ran_time_2 = str(ran_hour_2) + ':' + str(ran_minute_2)

    #Print random times
    print("""3 Messages had been sent today! Initializing new times:

Random times are:
1st: %s
2nd %s
3rd %s"""
    % (ran_time_0, ran_time_1, ran_time_2))

    return ran_time_0, ran_minute_1, ran_minute_2





#Sender, and Counter
while True:
    checker = 0
    ran_time_0, ran_time_1, ran_time_2 = random_times()

    while checker != 3 or checker < 3: #Amount of times, sent. Also is affected by the following if statement. --> Change to Increase/Decrease the amount of messages per day.
        now_time = current_time()
        
        if ((now_time == ran_time_0) or
            (now_time == ran_time_1) or
            (now_time == ran_time_2) or
            (now_time == now_time)):

            email_sender_to_military(times_sent, now_time)
            print("A new Message has been sent! %s" % now_time)
            checker += 1
            times_sent += 1
            time.sleep(60)
        
        else:
            time.sleep(60)
    
    #TO DO: EXIT SECOND LOOP HERE, AND MAKE IT SLEEP UNTIL THE NEXT DAY, THEN THE LOOP WILL GO AGAIN. --> To maximize efficiency 
