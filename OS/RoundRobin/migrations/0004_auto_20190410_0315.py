# Generated by Django 2.1.7 on 2019-04-09 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RoundRobin', '0003_auto_20190409_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Processed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('arrivalTime', models.PositiveIntegerField(default=0)),
                ('burstTime', models.PositiveIntegerField(default=0)),
                ('remainingTime', models.PositiveIntegerField(default=0)),
                ('waitingTime', models.PositiveIntegerField(default=0)),
                ('turnAroundTime', models.PositiveIntegerField(default=0)),
                ('priority', models.BooleanField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RoundRobin.UserQueue')),
            ],
        ),
        migrations.AlterField(
            model_name='process',
            name='priority',
            field=models.BooleanField(default=0),
        ),
    ]
