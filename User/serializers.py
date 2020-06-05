from rest_framework import serializers
from .models import User,ActivityPeriod

class TimezoneField(serializers.Field):
    #Take the timezone object and make it JSON serializable
    
    def to_representation(self, obj):
        return obj.zone

    def to_internal_value(self, data):
        return data

class ActivityPeriodSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format='%b %d %Y %H:%M %p')
    end_time = serializers.DateTimeField(format='%b %d %Y %H:%M %p')
    class Meta:
        model=ActivityPeriod
        fields=['start_time','end_time']

class UserSerializer(serializers.ModelSerializer):
    tz=TimezoneField()
    activity_periods = ActivityPeriodSerializer(many=True)
    class Meta:
        model=User
        fields=['id','real_name','tz','activity_periods']



