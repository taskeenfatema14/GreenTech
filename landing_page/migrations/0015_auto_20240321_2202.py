# Generated by Django 3.2.5 on 2024-03-21 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0014_brochure_category_landingimage_product_productitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Brochure',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductItem',
        ),
    ]
