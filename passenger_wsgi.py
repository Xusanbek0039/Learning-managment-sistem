import os
import sys

# Django loyihang joylashgan papkani sys.path ga qo'shamiz
sys.path.insert(0, os.path.dirname(__file__))

# Django settings modulini belgilaymiz (SMS — loyihangizning papka nomi bo'lsin)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SMS.settings')

# Django WSGI ilovasini yuklaymiz
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
