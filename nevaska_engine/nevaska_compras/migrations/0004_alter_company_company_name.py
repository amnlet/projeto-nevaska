# Generated by Django 5.0.6 on 2024-06-04 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nevaska_compras', '0003_alter_company_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]