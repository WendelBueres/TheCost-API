from django.db import models

class TypesChoices(models.TextChoices): 
    reward = "reward"
    debit = "debit"

class CategoryChoices(models.TextChoices):
    salary = "salary"
    bill = "bill"
    leisure = "leisure"
    shopping = "shopping"
    vehicle = "vehicle"

class Register(models.Model):
    description = models.TextField(max_length=128)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    type = models.CharField(
        max_length=7,
        choices=TypesChoices.choices
    )
    category = models.CharField(
        max_length=8,
        choices=CategoryChoices.choices
    )
    user = models.ForeignKey(
        "user.User", related_name="register", on_delete=models.CASCADE,
    )
