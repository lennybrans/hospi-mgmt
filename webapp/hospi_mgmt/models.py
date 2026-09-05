from django.db import models


# Create your models here.
class Availability(models.Model):
    """A hospi space and the type of animal it is dedicated to."""

    id = models.AutoField(primary_key=True)
    space = models.IntegerField(
        db_column="hospi",
        verbose_name="número de hospi",
        help_text="Número del hospi"
    )
    dedicated = models.CharField(
        db_column='type_of_animal',
        max_length=3,
        verbose_name="tipo de animal",
        help_text="Código corto del animal (GAT o PER)",
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
        db_table = 'availability'
        verbose_name_plural = 'Availabilities'
        ordering = ['space']


class Occupant(models.Model):
    """The animal occupying a hospi space, and its intake details."""

    occupant_id = models.AutoField(primary_key=True)
    space = models.OneToOneField(
        Availability,
        on_delete=models.CASCADE,
        db_column='space_occupant',
        related_name="occupant",
        verbose_name="espacio",
        error_messages={
            "unique": "Este espacio ya está ocupado."
        },
    )
    name = models.CharField(
        db_column="name_occupant",
        max_length=25,
        verbose_name="nombre",
        help_text="Nombre del animal"
    )
    weight = models.FloatField(
        db_column='weight_animal',
        verbose_name="peso",
        help_text="Peso del animal",
        blank=True,
        null=True
    )
    motive = models.CharField(
        db_column="motive",
        max_length=127,
        verbose_name="motivo de consulta",
        help_text="Motivo de consulta",
        blank=True,
        null=True
    )
    correa = models.CharField(
        db_column='correa_description',
        max_length=31,
        verbose_name="correa",
        help_text="Descripción correa",
        blank=True,
        null=True
    )
    transportin = models.CharField(
        db_column='transportin_description',
        max_length=31,
        verbose_name="transportín",
        help_text="Descripción transportín",
        blank=True,
        null=True
    )
    attention = models.TextField(
        db_column="attention",
        verbose_name="atención",
        help_text="Notas de atención",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
