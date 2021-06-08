# Generated by Django 3.2.3 on 2021-06-05 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotePads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_update', models.DateTimeField(auto_now=True)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('memo', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-datetime_update', '-datetime_created'],
                'abstract': False,
            },
        ),
    ]
