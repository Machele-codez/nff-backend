# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
from os import getenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='farouqimoro@gmail.com', # mine
    to_emails='farouqimoro3@gmail.com', # the admin's email comes
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
message.reply_to = 'smithbeblack@gmail.com' # the guy who is accessing the website
try:

    sg = SendGridAPIClient(getenv('SENDGRID_API_KEY'))
    print(getenv('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.args[0])
