# Generated by Django 4.2.7 on 2023-12-11 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TraineerbookApp', '0005_alter_activity_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='image',
            field=models.ImageField(null=True, upload_to='static'),
        ),
    ]