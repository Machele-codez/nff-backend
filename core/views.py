from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.shortcuts import redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def send_email(request):
    sender_email = request.POST.get('sender_email')
    sender_name = request.POST.get('sender_name')
    content = request.POST.get('content')
    subject = f'New Future Foundation: New email from {
        sender_name}'  # the subject
    admin_email = settings.ADMIN_EMAIL  # the one receiving the email

    message = Mail(
        from_email='no-reply@newfuturefoundation.org',  # mine
        to_emails=admin_email,  # the admin's email comes
        subject=subject,
        html_content=content)
    message.reply_to = sender_email  # the guy who is accessing the website
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
    except Exception as e:
        print(e.args[0])

    referer = request.META.get(
        'HTTP_REFERER', 'https://newfuturefoundation.org/contact-us.html')
    return redirect(referer)
