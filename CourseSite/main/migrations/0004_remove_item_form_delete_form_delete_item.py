# Generated by Django 5.0 on 2023-12-22 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_form1_date_alter_form1_fio_alter_form1_fullfio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='form',
        ),
        migrations.DeleteModel(
            name='Form',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]