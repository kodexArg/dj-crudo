# Generated by Django 4.0.4 on 2022-05-01 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='apellidos')),
                ('email', models.EmailField(max_length=50, verbose_name='correo electrónico')),
                ('telephone', models.CharField(max_length=50, verbose_name='nombre')),
                ('birth_date', models.DateField(blank=True, verbose_name='fecha de nacimiento')),
                ('nationality', models.CharField(choices=[('AR', 'Argentina'), ('BR', 'Brasil'), ('BO', 'Bolivia'), ('CH', 'Chile'), ('PA', 'Paraguay'), ('UR', 'Uruguay'), ('OT', 'Otro')], max_length=50, verbose_name='nacionalidad')),
                ('document', models.PositiveIntegerField(verbose_name='documento')),
                ('comment', models.TextField(blank=True, max_length=400, null=True, verbose_name='comentario del visitante')),
                ('survey_update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'ficha de encuesta',
                'verbose_name_plural': 'encuesta',
            },
        ),
    ]
