# Generated by Django 5.0.7 on 2024-07-31 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_skills_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='percent',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
