# Generated by Django 2.1.7 on 2019-04-22 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190422_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='back_View',
            field=models.ImageField(default='vsabre.jpg', upload_to='back', verbose_name='Back View'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='front_View',
            field=models.ImageField(default='vsabre.jpg', upload_to='front'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='interior_View',
            field=models.ImageField(default='vsabre.jpg', upload_to='interior', verbose_name='Interior View'),
        ),
    ]
