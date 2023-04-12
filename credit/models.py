from django.utils import timezone
from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    citizenship = models.CharField(max_length=20, null=True, default="кыргызстан")
    birth_yea = models.DateField(null=True, blank=True)
    work_place = models.CharField(max_length=30)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return self.name

class Account(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    number = models.CharField(max_length=16, null=True, blank=True)
    account_type = models.IntegerField(default=1, null=True)

    class Meta:
        db_table = 'accounts'


class Credit(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    sum = models.IntegerField(null=True, blank=True)
    date = models.DateField(default=timezone.now)

    class Meta:
        db_table = 'loans'