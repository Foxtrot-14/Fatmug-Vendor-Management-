# Generated by Django 5.0.4 on 2024-05-08 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_alter_purchaseorder_issue_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalperformance',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
