# Generated by Django 5.1.7 on 2025-03-20 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_jobtype_remove_jobs_job_type_jobs_jobtype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobtype',
            old_name='titlr',
            new_name='title',
        ),
    ]
