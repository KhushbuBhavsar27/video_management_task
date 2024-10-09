# Generated by Django 4.2.3 on 2024-10-09 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vd_name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('vd_file', models.FileField(upload_to='videos/')),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
