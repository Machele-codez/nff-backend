import logging
import threading

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

# Configure the logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


# Create your views here.

def send_notification_email(subject, message, recipient_list):
    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            recipient_list,
            fail_silently=False,
        )
        logger.info("Email sent successfully to %s", recipient_list)
    except Exception as e:
        logger.error("Failed to send email to %s. Error: %s",
                     recipient_list, str(e))


@csrf_exempt
def send_email(request):
    sender_email = request.POST.get('sender_email')
    sender_name = request.POST.get('sender_name')
    content = request.POST.get('content')

    # Mail Content
    subject = f'New Future Foundation: New email from {sender_name}'
    admin_email = 'smithbeblack@gmail.com'  # the one receiving the email
    message = f"You have received a new message from {
        sender_name} ({sender_email}).\nMessage: {content}"

    # Send email asynchronously
    threading.Thread(target=send_notification_email, args=(
        subject, message, [admin_email])).start()

    referer = request.META.get(
        'HTTP_REFERER', 'https://newfuturefoundation.org/contact-us.html')
    return redirect(referer)
