

python3 manage.py startapp base

python3 manage.py migrate 

python3 manage.py makemigrations

python3 manage.py migrate 

python3 manage.py createsuperuser

python3 manage.py runserver

# After creating of Topic and Message models, run the following commands to create migrations and apply them:
python3 manage.py makemigrations
python3 manage.py migrate

# Then go to admin.py and register the models:
from django.contrib import admin
from .models import Topic, Message
admin.site.register(Topic)
admin.site.register(Message)



