from django.db import models


# Create your models here.


#class Publisher(models.Model):
 #   first_name = models.CharField(max_length=30)
  #  last_name = models.CharField(max_length=30)
   # username = models.CharField(max_length=30)
    #email = models.EmailField(max_length=60)
   # password = models.CharField(max_length=20)


class dynamic(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField()
    describe = models.CharField(max_length=200)
    price = models.IntegerField()
