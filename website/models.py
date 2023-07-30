from django.db import models

# Create your models here.
class enquiry_table(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Telephone = models.CharField(max_length=10)
    Subject = models.CharField(max_length=10)
    Message = models.TextField()

    def __str__(self):
        return self.Name

class booking_form(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    destination = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name





