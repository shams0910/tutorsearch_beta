# Generated by Django 3.2.3 on 2021-08-03 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_company_company_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
