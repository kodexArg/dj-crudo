from django.db import models


class Survey(models.Model):
    """
    Initial poll model. Retrieves data from new customers.

    It could became the father class/model for incoming polls, so it's only focused on getting
    fields I don't expect to change, like personal data and social network mostly.
    """
    NATIONS = (
        ('AR', 'Argentina'),
        ('BR', 'Brasil'),
        ('BO', 'Bolivia'),
        ('CH', 'Chile'),
        ('PA', 'Paraguay'),
        ('UR', 'Uruguay'),
        ('OT', 'Otro'),
    )

    first_name      = models.CharField('nombre', max_length=50)
    last_name       = models.CharField('apellidos', max_length=50)
    email           = models.EmailField('correo electrónico', max_length=50)
    telephone       = models.CharField('teléfono', max_length=50)
    birth_date      = models.DateField('fecha de nacimiento', blank=True)
    nationality     = models.CharField('nacionalidad', max_length=50, choices=NATIONS)
    document        = models.PositiveIntegerField('documento')
    comment         = models.TextField('comentario del visitante', max_length=400, blank=True, null=True)
    survey_update   = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name = 'ficha de encuesta'
        verbose_name_plural = 'encuesta'
