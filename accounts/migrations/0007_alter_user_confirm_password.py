# Generated by Django 3.2.5 on 2024-03-09 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_confirm_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirm_password',
            field=models.CharField(max_length=16),
        ),
    ]
