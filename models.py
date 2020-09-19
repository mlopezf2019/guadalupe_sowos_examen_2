import uuid
from django.db import models

class User(models.Model):
  uuid = models.UUIDField(primary_key = False, default = uuid.uuid4, editable = False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Person(models.Model):
  user_id = models.ForeignKey(User)
  name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Customer(models.Model):
  person_id = models.ForeignKey(Person)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

