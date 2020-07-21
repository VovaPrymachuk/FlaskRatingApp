import smtplib
from email.mime.text import MIMEText


def send_mail(user, worker, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'fbb5c666ccf08b'
    password = 'b1212ecfabfcae'
    message = f'<h3>New Feedback<h3><ul>' \
              f'<li>User: {user}</li>' \
              f'<li>Worker: {worker}</li>' \
              f'<li>Rating: {rating}</li>' \
              f'<li>Comments: {comments}</li></ul>'

    sender_email = 'email1@example.com'
    received_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Worker feedback'
    msg['From'] = sender_email
    msg['To'] = received_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, received_email, msg.as_string())