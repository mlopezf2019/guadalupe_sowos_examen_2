import uuid
from django.db import models

class User(models.Model):
  uuid = models.UUIDField(primary_key = False, default = uuid.uuid4, editable = False)
  
class Person(models.Model):
  user_id = models.ForeignKey(User)
  name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)

class Customer(models.Model):
  person_id = models.ForeignKey(Person)

