import smtplib, ssl
from . import low_attendance_list as lal

def notify_people(Class_name):
    
    names,email,a = lal.low_attendance(Class_name)

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "facerec1234@gmail.com"
    password = "brnedwgnhzyvcftn"

    for eid in email:
        receiver_email = eid
        message = lal.message_content(eid)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            server.quit()
def main():
    notify_people("S8CSEa(old)")

if __name__ == "__main__":
    main()
