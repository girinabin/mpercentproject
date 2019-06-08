from django.db import models


class post(models.Model):
    firstname = models.CharField(max_length=50,)
    lastname = models.CharField(max_length=50)
    department = models.CharField(max_length=50,choices=(('tech', 'Tech'),
        ('mplab', 'Mplab'),
        ('acadmey', 'Acadmey')),default='DEFAULT VALUE')

    operations = models.CharField(max_length=50,choices=(('hall', 'Hall'),
        ('utensils', 'Utensils')),default='DEFAULT VALUE')





