# Generated by Django 3.0.4 on 2020-05-28 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('streets', '0002_auto_20200527_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('house', models.IntegerField()),
                ('time_to_close', models.TimeField()),
                ('time_to_open', models.TimeField()),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streets.Streets')),
            ],
        ),
    ]
