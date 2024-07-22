from django.db import models
from django.contrib.auth.models import User

class Problem(models.Model):
    PROGRESS_CHOICES = [
        ('processing', 'Processing'),
        ('resolved', 'Resolved'),
        ('escalated', 'Escalated'),
    ]
    
    problem_type = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    description = models.TextField()
    geo_location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='problems/', blank=True, null=True)
    progress = models.CharField(
        max_length=10,
        choices=PROGRESS_CHOICES,
        default='processing'
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.problem_type


class Funding(models.Model):
    upi_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.upi_id} - {self.amount}"