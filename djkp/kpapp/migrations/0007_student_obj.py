# Generated by Django 2.0.3 on 2018-03-29 02:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kpapp', '0006_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_obj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
