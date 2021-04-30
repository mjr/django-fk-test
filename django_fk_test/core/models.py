from django.db import models

from simple_history.models import HistoricalRecords


class Foo(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    history = HistoricalRecords()


class Bar(models.Model):
    NAME = "name"
    EMAIL = "email"
    PHONE = "phone"

    KINDS = (
        (NAME, "Name"),
        (EMAIL, "Email"),
        (PHONE, "Phone"),
    )

    ACCEPTED = "A"
    REJECTED = "R"
    UNDER_ANALYSIS = "U"

    STATUS_CHOICES = (
        (ACCEPTED, "Accepted"),
        (REJECTED, "Rejected"),
        (UNDER_ANALYSIS, "Under Analysis"),
    )

    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    kind = models.CharField(max_length=5, choices=KINDS)
    foo = models.ForeignKey("Foo", on_delete=models.CASCADE)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default=UNDER_ANALYSIS
    )

    history = HistoricalRecords()
