# Generated by Django 2.1.7 on 2019-05-06 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm_practice_app', '0005_auto_20190506_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]