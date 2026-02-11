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


class Material(models.Model):
    name = models.CharField(
        db_column='attribute_name',
        max_length=20,
        help_text='Nombre del attributo'
    )

    def __str__(self):
        return self.name


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
        help_text="Peso del animal"
    )
    motive = models.CharField(
        db_column="motive",
        max_length=127,
        help_text="Motivo de consulta"
    )
    attention = models.TextField(
        db_column="attention",
        help_text="Attention"
    )
    material = models.ManyToManyField(
        Material,
        db_column="material_name",
        help_text="Correa o/y Transportín",
        blank=True
    )

    def __str__(self):
        return self.name
