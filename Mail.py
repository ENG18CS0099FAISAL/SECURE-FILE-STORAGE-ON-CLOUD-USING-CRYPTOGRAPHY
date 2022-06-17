import smtplib
gmail_user ="faisalssheriff@gmail.com"
gmail_password = "msgbyzgjalwiaxrf"
def send_email(subject, msg, to):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(gmail_user, to, message)
        server.close()
        print("Success: Email sent!")
    except Exception as e:
        print(e)
        print("Email failed to send.")
send_email("HELLO","test","faisalssheriff@gmail.com")
