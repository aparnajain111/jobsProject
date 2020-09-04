import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobsProject.settings')

import django
django.setup()

from jobsapp.models import hydjobs
from faker import Faker
from random import *
fake = Faker()

def phonenumbergen():
    d1=randint(7,9)
    num =''+str(d1)
    for i in range(9):
        num += str(randint(0,9))
    return int(num)    

def populate(num):
    for i in range(num):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager',
        'Team Lead','Software Engineer'))
        feligibility = fake.random_element(elements=('B.Tech','M.Tech','MCA','Phd'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        hyd_records = hydjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,
        eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)

populate(25)        