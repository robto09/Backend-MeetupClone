# Generated by Django 2.1 on 2018-08-30 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='myuser',
            name='activation_token',
            field=models.CharField(default=1, max_length=40, verbose_name='activation token'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='firstname',
            field=models.CharField(default=1, max_length=120, verbose_name='first name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='lastname',
            field=models.CharField(default=1, max_length=120, verbose_name='last name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='username',
            field=models.CharField(default=1, max_length=255, unique=True, verbose_name='username'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]