from django.db import models


class LibraryRecord(models.Model):
    student_id = models.CharField(max_length=10)
    has_fines = models.BooleanField(default=False)
    amount_due = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"LibraryRecord - {self.student_id}"