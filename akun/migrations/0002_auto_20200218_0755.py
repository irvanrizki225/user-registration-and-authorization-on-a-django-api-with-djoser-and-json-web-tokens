# Generated by Django 3.0.3 on 2020-02-18 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('akun', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='update_on',
            new_name='updated_on',
        ),
    ]
