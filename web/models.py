from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Token(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  token = models.CharField(max_length=48)


class Expense(models.Model):
  text = models.CharField(max_length=255)
  date = models.DateTimeField()
  amount = models.BigIntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __unicode__(self):
    return self.text


class Income(models.Model):
  text = models.CharField(max_length=255)
  date = models.DateTimeField()
  amount = models.BigIntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __unicode__(self):
    return self.text
