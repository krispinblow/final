<<<<<<< HEAD

from django.core.mail import send_mail
from .models import Order

def order_created(order_id):
    """
    Send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    # when placed within the parentheses, there is no need for line continuations
    message = ( 
                f'Dear {order.first_name},\n\n'
                f'You have successfully placed an order.'
                f'Your order ID is {order.id}.' 
              )
    mail_sent = send_mail(subject,
                          message,
                          'krispinblow@gmail.com',
                          [order.email])
    return mail_sent

=======

from django.core.mail import send_mail
from .models import Order

def order_created(order_id):
    """
    Send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    # when placed within the parentheses, there is no need for line continuations
    message = ( 
                f'Dear {order.first_name},\n\n'
                f'You have successfully placed an order.'
                f'Your order ID is {order.id}.' 
              )
    mail_sent = send_mail(subject,
                          message,
                          'krispinblow@gmail.com',
                          [order.email])
    return mail_sent

>>>>>>> cee217ef8247483092a4e186f2cbb868d393e645
