# Generated by Django 3.1.6 on 2022-06-28 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_whatwearereadinglink_wwar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whatwearereadinglink',
            name='wwar',
        ),
        migrations.AlterField(
            model_name='whatwearereadinglink',
            name='wwar_link',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='news.whatwearereading'),
        ),
    ]
