# Generated by Django 2.1.5 on 2019-02-13 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thewall', '0009_auto_20190213_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brick',
            name='wall_page',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bricks', to='thewall.WallPage', verbose_name='message wall'),
        ),
    ]
