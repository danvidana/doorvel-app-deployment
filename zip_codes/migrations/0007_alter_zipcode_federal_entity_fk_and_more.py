# Generated by Django 4.1.7 on 2023-03-05 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zip_codes', '0006_municipality_local_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zipcode',
            name='federal_entity_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zip_codes.federalentity'),
        ),
        migrations.AlterField(
            model_name='zipcode',
            name='municipality_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zip_codes.municipality'),
        ),
    ]
