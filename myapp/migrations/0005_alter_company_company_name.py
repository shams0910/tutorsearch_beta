# Generated by Django 3.2.3 on 2021-07-23 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210722_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(default='Company name', max_length=25, null=True),
        ),
    ]
