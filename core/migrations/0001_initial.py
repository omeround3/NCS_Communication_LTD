# Generated by Django 3.2.3 on 2021-05-22 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('cellphone', models.IntegerField()),
                ('bandwidth', models.CharField(choices=[('150', '150 Mbps'), ('500', '500 Mbps'), ('1000', '1 Gbps')], default='500', max_length=4)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('cost', models.IntegerField(default=150)),
            ],
        ),
    ]
