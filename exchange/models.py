from django.db import models

# Create your models here.


class ConversionHistory(models.Model):
    source_currency=models.CharField(max_length=3)
    target_currency=models.CharField(max_length=3)
    amount=models.DecimalField(max_digits=30,decimal_places=2)
    converted_amount = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} {self.source_currency} to {self.target_currency}"

    
