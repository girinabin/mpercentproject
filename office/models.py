from django.db import models
from multiselectfield import MultiSelectField

class post(models.Model):
    CHOICES1 = (
        ('11', 'Tech'),
        ('22', 'Mplab'),
        ('23', 'Acadmey')
    )
    CHOICES2 = (
        ('11', 'Hall'),
        ('22', 'Utensils')
    )

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    department = MultiSelectField(choices = CHOICES)
    operations = MultiSelectField(choices = CHOICES1)




