# Generated by Django 2.1.5 on 2019-02-13 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thewall', '0008_auto_20190205_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brick',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name'),
        )
    ]