import random
import string
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save

def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def fill_username(instance, **kwargs):
    if not instance.username:
        username =  "from_email" + id_generator(15)
        while len(User.objects.filter(username = username)) > 0:
            username =  "from_email" + id_generator(15)
        instance.username = username

pre_save.connect(fill_username, sender=User)
