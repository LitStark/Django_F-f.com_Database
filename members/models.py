from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=10, null=True)
    city = models.CharField(max_length=255, default='kota')
    state = models.CharField(max_length=20, default='Rajasthan')

    class Meta:
        verbose_name_plural = 'Membars'

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    dob=models.DateField(null=True, blank=True)
    gender=models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):
        return f'{self.user}'