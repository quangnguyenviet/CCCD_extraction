from django.db import models


class IDCardRecord(models.Model):

    class StatusChoices(models.TextChoices):
        SUCCESS = "success", "Success"
        FAILED = "failed", "Failed"

    id_number = models.CharField(max_length=20)
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    hometown = models.TextField()

    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.SUCCESS
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} - {self.id_number}"