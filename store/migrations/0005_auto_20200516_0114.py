# Generated by Django 3.0.6 on 2020-05-15 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200516_0112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='quality',
            new_name='quantity',
        ),
    ]
