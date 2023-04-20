from django.db import models

# Create your models here.
class Student(models.Model):
    FirstName=models.CharacterField(max_length=200)
    LastName=models.CharacterField(max_length=200)
    Contact=models.CharacterField(max_length=200)
    NIN=models.CharacterField(max_length=30)
    Photo=models.ImageField(upload_to ='uploads/')
    GENDER_CHOICES = [
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
   ]
    GENDER = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    DATEOFBIRTH = models.DateField()

   
    