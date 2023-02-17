# Generated by Django 4.1.3 on 2022-11-27 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demooapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
