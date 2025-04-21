from djongo import models

class Consumer(models.Model):
    _id = models.ObjectIdField()
    Customer = models.IntegerField(unique=True)
    Postcode = models.IntegerField()

    class Meta:
        abstract = True  # Critical for MongoDB
        managed = False  # Prevents Django from creating tables

    @classmethod
    def get_collection(cls):
        from ..energy_data.mongo_connection import get_mongo_collection
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
        from ..energy_data.mongo_connection import get_mongo_collection
        return get_mongo_collection('energy_records')