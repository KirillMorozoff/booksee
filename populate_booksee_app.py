import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booksee.settings')

import django
django.setup()

##FAKE POP SCRIPT
import random
from booksee_app.models import AccessRecord, Webpage, Topic
from faker import Faker
fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
