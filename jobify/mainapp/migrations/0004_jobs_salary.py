# Generated by Django 5.1.7 on 2025-03-20 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_jobs_close_date_alter_jobs_open_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
