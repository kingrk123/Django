# Generated by Django 2.2.5 on 2019-09-19 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SavingAccount',
            fields=[
                ('Accno', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=10)),
                ('Balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
    ]
