# Generated by Django 3.2.5 on 2024-03-09 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_user_confirm_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
