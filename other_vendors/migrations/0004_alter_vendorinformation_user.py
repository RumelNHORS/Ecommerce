# Generated by Django 4.2.3 on 2023-10-04 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('other_vendors', '0003_vendorinformation_vendor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorinformation',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vendorinformation', to=settings.AUTH_USER_MODEL),
        ),
    ]
