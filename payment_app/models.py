from django.db import models


class Payment(models.Model):
    student_id = models.CharField(max_length=10)
    amount_paid = models.DecimalField(max_digits=6, decimal_places=2)
    date_paid = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Payment - {self.student_id}"