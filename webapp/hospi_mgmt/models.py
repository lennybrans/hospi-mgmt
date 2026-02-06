from django.db import models


# Create your models here.
class Occupant(models.Model):
    pk_id = models.AutoField(
        db_column="pk",
        primary_key=True
    )
    name = models.CharField(
        db_column="name_occupant",
        max_length=25,
        verbose_name="occupant",
        help_text="Name of the occupant"
    )
