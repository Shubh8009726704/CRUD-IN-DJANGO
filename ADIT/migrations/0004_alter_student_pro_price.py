# Generated by Django 4.1.10 on 2023-08-18 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADIT', '0003_alter_student_pro_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pro_price',
            field=models.IntegerField(),
        ),
    ]