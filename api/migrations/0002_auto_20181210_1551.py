# Generated by Django 2.1.2 on 2018-12-10 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrower',
            name='token_id',
        ),
        migrations.RemoveField(
            model_name='subadmin',
            name='token_id',
        ),
        migrations.RemoveField(
            model_name='superadmin',
            name='token_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='token_id',
        ),
        migrations.DeleteModel(
            name='Token',
        ),
    ]