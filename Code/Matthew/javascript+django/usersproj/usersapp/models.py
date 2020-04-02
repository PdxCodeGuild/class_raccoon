from django.db import models


# from django.contrib.auth.models import User
# class MyModel(models.Model):
#   user = models.ForiegnKey(User, on_delete=models.PROTECT)
#   ...



from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  phone = models.CharField(max_length=20)
  location = models.CharField(max_length=100)
  image = models.ImageField(upload_to='profile_images/', null=True, blank=True)


  def __str__(self):
    return self.username


# less good way =============================================

# from django.contrib.auth.models import User

# class UserProfile(models.Model):
#   user = models.OneToOneField(User, related_name='user_profile')
#   phone = models.CharField(max_length=20)
#   location = models.CharField(max_length=100)

# class TodoItem(models.Model):
#   text = models.CharField(max_length=200)
#   user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

#   def __str__(self):
#     return self.user_profile.user.username + ' ' + self.text

# @login_required
# def index(request):
#   location = request.user.user_profile.location









# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#   phone = models.CharField(max_length=20)

