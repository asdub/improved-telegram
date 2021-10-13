# Generated by Django 3.2.7 on 2021-10-13 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(default='Pending', max_length=32),
        ),
    ]
