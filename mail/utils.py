# encoding: utf-8
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

def send_mail(to_emails, from_email, subject,
    text_template='mail/message.txt',
    data={}):
    """
    Function for sending email both in HTML and text formats.
    to_emails - list of emails for sending
    from_email - sender address
    subject - the subject of message
    text_template - template for text mail
    html_template - template for html mail
    data - dictionary with data for templates
    """
    text_content = render_to_string(text_template, data)
    msg = EmailMultiAlternatives(subject, text_content, from_email, to_emails)
    msg.send()
