from django.db import models
from django.core.validators import RegexValidator


class Camera(models.Model):

    SERIAL_LENGTH = 16

    serial_validator = RegexValidator(
        regex=r'^[0-9A-F]{16}$',
        message="Only " + str(SERIAL_LENGTH) + " char length, hex values are allowed.",
    )

    serial_number = models.CharField(
        primary_key=True,
        max_length=SERIAL_LENGTH,
        validators=[serial_validator],
    )

    def __str__(self):
        return self.serial_number


class Room(models.Model):

    MAX_NAME_LENGTH = 50

    name = models.CharField(
        unique=True,
        max_length=MAX_NAME_LENGTH,
    )

    camera = models.OneToOneField(
        'Camera',
        null=True,
        on_delete=models.SET_NULL,
    )

    maximum_capacity = models.PositiveIntegerField(
        default=1,
    )

    number_of_requests = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self):
        return self.name
