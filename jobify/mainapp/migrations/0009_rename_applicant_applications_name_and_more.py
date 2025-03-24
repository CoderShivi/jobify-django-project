# Generated by Django 5.1.7 on 2025-03-21 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_rename_titlr_jobtype_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applications',
            old_name='applicant',
            new_name='name',
        ),
        migrations.AddField(
            model_name='applications',
            name='cover_letter',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applications',
            name='email',
            field=models.EmailField(default='user@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='applications',
            name='phone',
            field=models.CharField(default='000-000-0000', max_length=15),
        ),
    ]
