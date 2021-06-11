# Generated by Django 2.1.5 on 2021-06-01 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('summary', models.TextField(default='This is cool!')),
            ],
        ),
    ]
