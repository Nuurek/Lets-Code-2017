from django.db import models
from django.core.validators import RegexValidator


class Camera(models.Model):

    SERIAL_LENGTH = 16

    serial_validator = RegexValidator(
        regex=r'^[0-9A-F]{16}$',
        message="Only " + str(SERIAL_LENGTH) + " char length, hex values are allowed."
    )

    serial_number = models.CharField(
        unique=True,
        max_length=SERIAL_LENGTH,
        validators=[serial_validator]
    )


class Room(models.Model):

    name = models.CharField(
        unique=True,
        max_length=50,
    )

    camera = models.ForeignKey(
        'Camera',
        null=True,
        on_delete=models.SET_NULL,
    )

    maximum_capacity = models.PositiveIntegerField()

    number_of_requests = models.PositiveIntegerField()
