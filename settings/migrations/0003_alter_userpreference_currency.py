# Generated by Django 5.0.1 on 2024-06-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_alter_userpreference_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreference',
            name='currency',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
