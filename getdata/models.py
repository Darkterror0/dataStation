import datetime

from django.db import models
import mongoengine

class finance(mongoengine.Document):
    abstract=mongoengine.StringField(max_length=20,)
    checkPeople=mongoengine.StringField(max_length=20)
    city=mongoengine.StringField(max_length=20)
    cityarea = mongoengine.StringField(max_length=20)
    classify = mongoengine.StringField(max_length=20)
    FEATURE = mongoengine.StringField(max_length=100)
    indicatorOfAdvert = mongoengine.IntField(default=0)
    indicatorOfComplaint = mongoengine.IntField(default=0)
    indicatorOfIllegal = mongoengine.IntField(default=0)
    indicatorOfIncome = mongoengine.IntField(default=0)
    indicatorOfInfluence = mongoengine.IntField(default=0)
    modifyDate = mongoengine.DateField(default=datetime.datetime.now)
    monitorCompanySource = mongoengine.StringField(max_length=200)
    monitorTime = mongoengine.DateField()
    name = mongoengine.StringField(max_length=200)
    province = mongoengine.StringField(max_length=20)
    RATEOFRETURN = mongoengine.IntField(default=0)
    score = mongoengine.IntField(default=0)
    shortname = mongoengine.StringField(max_length=20)
    state = mongoengine.StringField(max_length=20)
    status = mongoengine.IntField(default=0)
    url = mongoengine.StringField(max_length=50)
