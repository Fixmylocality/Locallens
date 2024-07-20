from django.db import models
from django.contrib.auth.models import User

class Problem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    locality = models.CharField(max_length=255)
    problem_type = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='problems/')
    geo_location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
