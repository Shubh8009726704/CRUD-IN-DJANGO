# Generated by Django 4.1.10 on 2023-08-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADIT', '0002_rename_address_student_pro_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pro_price',
            field=models.IntegerField(max_length=50),
        ),
    ]
