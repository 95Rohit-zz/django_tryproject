import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','try.settings')
import django
django.setup()
from hello.models import Topic, Info
from faker import Faker
fake = Faker()

def add_topic(number):
    t = Topic.objects.get_or_create(ID_number=number)[0]
    t.save()
    return t

def populate(N):
    q = 1
    for entry in range(N):
        top = add_topic(q)
        fakeFirst = fake.first_name()
        fakeLast = fake.last_name()
        fakeemail =fake.email()
        q = q+1

        info = Info.objects.get_or_create(num=top,First=fakeFirst,Last=fakeLast,email=fakeemail)[0]

if __name__ == '__main__':
    print("DING DING")
    populate(20)
    print("DONE")
