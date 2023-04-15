
from celery import shared_task
from time import sleep

@shared_task
def notify_customers(message):
    print('sending 10k emails')
    print(message)
    sleep(10)
    print('Emails were successufully sent!')
    