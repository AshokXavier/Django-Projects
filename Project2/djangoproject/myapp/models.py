from django.db import models

# Create your models here.
class Pet(models.Model):
  pet_name=models.CharField(max_length=40)
  pet_type=models.CharField(max_length=40)
  price=models.IntegerField()
  owner=models.CharField(max_length=40)
  phone_no=models.CharField(max_length=15)
  image=models.ImageField(upload_to='petshops/')

  def __str__(self):
    return self.pet_name