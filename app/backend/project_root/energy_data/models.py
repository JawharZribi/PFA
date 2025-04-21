from djongo import models
from django.contrib.auth.hashers import make_password, check_password
from mongoengine import Document, StringField


class Consumer(models.Model):
    _id = models.ObjectIdField()
    Customer = models.IntegerField(unique=True)
    Postcode = models.IntegerField()

    class Meta:
        abstract = True  # Critical for MongoDB
        managed = False  # Prevents Django from creating tables

    @classmethod
    def get_collection(cls):
        from .mongo_connection import get_mongo_collection
        return get_mongo_collection('consumers')

class EnergyRecord(models.Model):
    _id = models.ObjectIdField()
    Customer = models.IntegerField()  # Just a regular field, not ForeignKey
    Postcode = models.IntegerField()
    date = models.DateField()
    consumption = models.FloatField()
    # ... other fields ...

    class Meta:
        abstract = True  # Critical for MongoDB
        managed = False  # Prevents Django from creating tables

    @classmethod
    def get_collection(cls):
        from .mongo_connection import get_mongo_collection
        return get_mongo_collection('energy_records')
    
    from mongoengine import Document, StringField

from mongoengine import Document, StringField

class SuperUser(Document):
    meta = {"collection": "superusers"}  # optional, name of your MongoDB collection
    username = StringField(required=True, unique=True)
    password = StringField(required=True)

    @property
    def is_authenticated(self):
        return True
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)