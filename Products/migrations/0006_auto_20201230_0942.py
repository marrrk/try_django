# Generated by Django 2.1.5 on 2020-12-30 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_auto_20201229_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]