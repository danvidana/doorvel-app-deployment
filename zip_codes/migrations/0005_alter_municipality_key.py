# Generated by Django 4.1.7 on 2023-03-05 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zip_codes', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipality',
            name='key',
            field=models.CharField(max_length=120, primary_key=True, serialize=False),
        ),
    ]
