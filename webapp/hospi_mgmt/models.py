from django.db import models


# Create your models here.
class Availability(models.Model):
    space = models.IntegerField(
        db_column="hospi",
        verbose_name="hospi number",
        help_text="Number of the hospi"
    )
    dedicated = models.CharField(
        db_column='type_of_animal',
        max_length=3,
        help_text="Short code of animal (GAT or PER)",
        choices=[("GAT", "cat"), ("PER", "dog")]
    )

    def __str__(self):
        if self.occupied:
            state = "Occupado"
        else:
            state = "Libre"
        return f"{self.space} - {self.dedicated}: {state}"

    @property
    def occupied(self):
        return hasattr(self, "occupant")

    class Meta:
        verbose_name_plural = 'Availabilities'


class Occupant(models.Model):
    space = models.OneToOneField(
        Availability,
        on_delete=models.CASCADE,
        db_column='space_occupant',
        related_name="occupant",
        help_text="Eliga un espacio",
        error_messages={
            "unique": "Este espacio ya está ocupado."
        },
    )
    name = models.CharField(
        db_column="name_occupant",
        max_length=25,
        verbose_name="occupant",
        help_text="Nombre del animal"
    )
    weight = models.FloatField(
        db_column='weight_animal',
        help_text="Peso del animal",
        blank=True
    )
    motive = models.CharField(
        db_column="motive",
        max_length=127,
        help_text="Motivo de consulta",
        blank=True
    )
    correa = models.CharField(
        db_column='correa_description',
        max_length=31,
        help_text="Descripción correa",
        blank=True
    )
    transportin = models.CharField(
        db_column='transportin_description',
        max_length=31,
        help_text="Descripción transportín",
        blank=True
    )
    attention = models.TextField(
        db_column="attention",
        help_text="Attention",
        blank=True
    )

    def __str__(self):
        return self.name
