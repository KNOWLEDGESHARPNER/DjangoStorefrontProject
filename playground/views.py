from django.shortcuts import render
from django.core.mail import send_mail,mail_admins,EmailMessage,BadHeaderError
from templated_mail.mail import BaseEmailMessage
# from .tasks import notify_customers
import requests
from rest_framework.views import APIView
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
import logging

logger=logging.getLogger(__name__)

class HellowView(APIView):
    # @method_decorator(cache_page(5*10))
    def get(self,request):
        try:
            logger.info('Opening httpbin')
            response=requests.get('https://httpbin.org/delay/2')   
            logger.info('Recived httpbin response')
            data=response.json()
        except requests.ConnectionError:
            logger.critical('Httpbin is offline')
        return render(request, 'hello.html', {'name': data})
            


