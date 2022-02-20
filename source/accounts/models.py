from django.contrib.auth import get_user_model
from django.db import models


# class Profile(models.Model):
#     user = models.OneToOneField(get_user_model(), related_name="profile", on_delete=models.CASCADE, verbose_name='Profile')
#     about_me= models.TextField(max_length=500, null=True, blank=True,  verbose_name="About Me")
#     git_link = models.CharField(max_length="200", blank=True, null=True, verbose_name='GitHub Link')
#     avatar = models.ImageField(verbose_name="Profile Picture", upload_to="avatars/", null=True, blank=True)
#
#
#     class Meta:
#         verbose_name = 'Profile'
#         verbose_name_plural = 'Profiles'
#
#
#     def __str__(self):
#         return f"Profile: {self.user.username}. {self.id}"