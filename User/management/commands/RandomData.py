#  Creates random dummy data for n users .
#  N should be given by the user. 
#  Uses Faker to generate dummy data
from django.core.management.base import BaseCommand
from django.utils import timezone
import argparse
from faker import Faker
from User.models import User,ActivityPeriod
parser=argparse.ArgumentParser()

class Command(BaseCommand):

    def add_arguments(self,parser):
        parser.add_argument('number_of_users',action='store',type=int, help="Number of users to be created")

    def handle(self, *args, **kwargs):
        fake=Faker()
        activity_periods=[]
        for i in range(1000,1050):
            a=ActivityPeriod(id =i ,start_time=fake.date_time(),end_time=fake.date_time())
            a.save()

        for _ in range(kwargs['number_of_users']):
            pkid=fake.bothify(text='???##?#??').upper()
            name=fake.name()
            timezone=fake.timezone()
            User(id=pkid ,real_name=name , tz= timezone).save()
            user=User.objects.get(id=pkid)
            print("Created User", pkid, name, timezone)
            for _ in range(fake.random_int(min=1 ,max=5)):
                rnum=fake.random_int(min=1000, max=1050)
                ap=ActivityPeriod.objects.filter(id=rnum).first()
                user.activity_periods.add(ap)
        print("\n" ,kwargs['number_of_users'],"Users created successfully")
        
