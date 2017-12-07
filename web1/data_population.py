import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'web1.settings')

import django
django.setup()

from Discount_Collection.models import Topic, Webpage, AccessRecord

def populate():
    webpage = Webpage.objects.get_or_create()

if __name__ == '__main__':
    print("Populating data")
    populate()
    print("Complete")