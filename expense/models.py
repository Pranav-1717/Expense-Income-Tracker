from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.utils.timezone import now # type: ignore

# Create your models here.
class AddExpense(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    amount = models.FloatField()
    category = models.TextField(max_length=20)
    description = models.TextField(max_length = 50)
    date = models.DateField(default = now)

class AddIncome(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    amount = models.FloatField()
    category = models.TextField(max_length=20)
    description = models.TextField(max_length = 50)
    date = models.DateField(default = now)