from django.db import models

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    cellphone = models.CharField(max_length=15)
    SUBSCRIPTION = [
        ('150', '150 Mbps'),
        ('500', '500 Mbps'),
        ('1000', '1 Gbps'),
    ]
    bandwidth = models.CharField(
        max_length=4, choices=SUBSCRIPTION, default='500')
    start_date = models.DateField(auto_now_add=True)
    cost = models.IntegerField(default=150)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
