# Generated by Django 2.1.2 on 2018-10-07 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeCareApp', '0003_auto_20181007_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_no', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=1000)),
                ('text', models.CharField(max_length=100000)),
            ],
        ),
    ]