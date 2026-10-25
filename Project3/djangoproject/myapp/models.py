from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.

# one to one
# class Profile(models.Model):
#   user=models.OneToOneField(User,on_delete=models.CASCADE)
#   phone=models.CharField(max_length=50)
#   address=models.CharField(max_length=50)

#   def __str__(self):
#     return self.user.username

# One- to - many

# class Department(models.Model):
#   name=models.CharField(max_length=50)

#   def __str__(self):
#     return self.name

# class Employee(models.Model):
#   name=models.CharField(max_length=50)
#   salary=models.IntegerField()
#   department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name="employees")

#   def __str__(self):
#     return self.name

# # many to many

# from django.db import models

# class Course(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# class Student(models.Model):
#     name = models.CharField(max_length=100)

#     courses = models.ManyToManyField(
#         Course,
#         related_name="students"
#     )

#     def __str__(self):
#         return self.name

class Author(models.Model):
        name = models.CharField(max_length=100)
        country = models.CharField(max_length=100)
        def __str__(self):
                return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_date = models.DateField()
    stock = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    def __str__(self):
         return self.name
