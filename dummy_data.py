import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()


from faker import Faker
from products.models import Product , Brand
import random


def dummy_brand(n):
    fake = Faker()
    images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg']
    
    for x in range(n):
        Brand.objects.create(
            name = fake.name() , 
            image = f"brand/{images[random.randint(0,5)]}"
        )
    print(f'{n} Brand Done')



dummy_brand(100)