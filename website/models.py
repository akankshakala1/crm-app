from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")

class UserRole(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ROLE_CHOICES = (
        ('Manager', 'Manager'),
        ('Sales', 'Sales'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Sales')

    def __str__(self):
        return f"{self.user.username} - {self.role}"
