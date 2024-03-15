from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  phone = models.CharField(max_length=20, blank=True)
  address1 = models.CharField(max_length=100, blank=True)
  address2 = models.CharField(max_length=100, blank=True)
  city = models.CharField(max_length=100, blank=True)
  postcode = models.CharField(max_length=100, blank=True)

  def __str__(self):
    return f"{self.user.username} has firstname: {self.user.first_name} and email: {self.user.email}"

def create_profile(sender, instance, created, **kwargs):
  if created:
    user_profile = Profile(user=instance)
    user_profile.save()

post_save.connect(create_profile, sender=User)