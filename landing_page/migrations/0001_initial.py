# Generated by Django 4.2 on 2024-02-21 06:13

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/media_files')),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('-created_on',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LandingImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/media_files')),
                ('video', models.FileField(blank=True, null=True, upload_to='static/media_files', validators=[django.core.validators.FileExtensionValidator(['mp4', 'avi', 'mov'])])),
            ],
            options={
                'ordering': ('-created_on',),
                'abstract': False,
            },
        ),
    ]
