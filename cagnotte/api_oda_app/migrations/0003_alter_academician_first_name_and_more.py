# Generated by Django 4.0.2 on 2022-02-10 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_oda_app', '0002_payment_payment_hour_alter_payment_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academician',
            name='first_name',
            field=models.CharField(blank=True, max_length=40, verbose_name='prenom'),
        ),
        migrations.AlterField(
            model_name='academician',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='nom'),
        ),
        migrations.AlterField(
            model_name='academician',
            name='picture',
            field=models.FileField(blank=True, upload_to='pictures', verbose_name='photos'),
        ),
        migrations.AlterField(
            model_name='academician',
            name='register_number',
            field=models.CharField(blank=True, max_length=30, verbose_name='matricule'),
        ),
    ]
