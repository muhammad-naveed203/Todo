# Generated by Django 4.1.1 on 2022-09-08 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_alter_todoitem_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
