# Generated by Django 3.1.3 on 2021-01-05 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_auto_20210104_1733'),
        ('posts', '0027_auto_20210105_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='groups.group'),
        ),
    ]