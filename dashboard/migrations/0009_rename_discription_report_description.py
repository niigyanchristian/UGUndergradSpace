# Generated by Django 4.0.3 on 2022-04-27 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_report_viewers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='discription',
            new_name='description',
        ),
    ]