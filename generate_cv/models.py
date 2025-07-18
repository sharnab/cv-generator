from django.db import models

# Create your models here.
class Info(models.Model):
    basics = models.JSONField(blank=False, null=False)
    education = models.JSONField(blank=True, null=True)
    experience = models.JSONField(blank=True, null=True)
    projects = models.JSONField(blank=True, null=True)
    skills = models.JSONField(blank=True, null=True)
    languages = models.CharField(max_length=255, blank=True, null=True)
    contacts = models.JSONField(blank=True, null=True)
    profile = models.JSONField(blank=True, null=True)
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.basics