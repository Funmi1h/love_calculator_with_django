from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class LoveResult(models.Model):
    name1 = models.CharField(
        max_length= 155,
        verbose_name= 'name1',
        blank= False,
        null= True)
    
    name2 = models.CharField(
        max_length= 155,
        verbose_name= 'name1',
        blank= False,
        null= True)
    
    percentage = models.DecimalField(
        max_digits= 4, 
        decimal_places= 2,
        verbose_name= 'percentage',
        null = True,
        blank= True)
    
    
    def __str__(self):
        return f"{self.name1} && {self.name2} = {self.percentage}"
