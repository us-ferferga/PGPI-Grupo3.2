# Generated by Django 4.2.7 on 2023-12-11 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TraineerbookApp', '0003_alter_activity_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='description',
            new_name='name',
        ),
    ]