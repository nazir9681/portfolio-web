# Generated by Django 3.1.5 on 2021-01-27 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
