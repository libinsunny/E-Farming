# Generated by Django 3.0.4 on 2020-05-03 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0004_auto_20200503_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='applicationNotice',
            field=models.FileField(default='', upload_to='application/documents'),
        ),
    ]