from django.db import models
from users.models import Custom_user

# Create your models here.

class Maids(models.Model):

    maid = models.ForeignKey(Custom_user, on_delete=models.CASCADE, related_name='maids')
    company_pay = models.DecimalField(max_digits=10, decimal_places=2)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    experience = models.IntegerField()
    work_location = models.CharField(max_length=100)
    salary_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Maids {self.maid} - {self.work_location}"