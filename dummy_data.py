import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()


from faker import Faker
from products.models import Product , Brand , Category , ProductReviews
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


def dummy_Category(n):
    fake = Faker()
    images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg']
    
    for x in range(n):
        Category.objects.create(
            name = fake.name() , 
            image = f"category/{images[random.randint(0,5)]}"
        )
    print(f'{n} Category Done')





def dummy_products(n):
    fake = Faker()
    images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg']
    flag = ['new','features','sale']

    for x in range(n):
        Product.objects.create(
            name = fake.name() , 
            subtitle = fake.text(max_nb_chars=400) , 
            description = fake.text(max_nb_chars=10000),
            image = f"product/{images[random.randint(0,5)]}" , 
            price = round(random.uniform(20.99,99.99),2),
            SKU = random.randint(100,10000) , 
            flag = flag[random.randint(0,2)],
            brand = Brand.objects.get(id=random.randint(8,100)),
            category = Category.objects.get(id=random.randint(1,100))
        )
    print(f'{n} Product Done')


def dummy_reviews(n):
    fake = Faker()
    
    for x in range(n):
        ProductReviews.objects.create(
            product = Product.objects.get(id=random.randint(1,1000)),
            name = fake.name(),
            image = 'reviews/default.jpg' , 
            rate = random.randint(1, 5),
            reviews = fake.text(max_nb_chars=300)
        )

    print(f'{n} Product Reviews Done')

# dummy_Category(100)
# dummy_products(1000)
dummy_reviews(3000)
