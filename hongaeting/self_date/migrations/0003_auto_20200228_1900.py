# Generated by Django 2.2.9 on 2020-02-28 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('self_date', '0002_auto_20200223_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinhistory',
            name='profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='profiles.Profile'),
        ),
    ]
