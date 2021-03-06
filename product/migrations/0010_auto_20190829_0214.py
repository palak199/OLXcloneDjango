# Generated by Django 2.2.4 on 2019-08-29 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_productimages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimages',
            options={'verbose_name': 'product image', 'verbose_name_plural': 'product images'},
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
