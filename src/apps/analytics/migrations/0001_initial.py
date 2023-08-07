# Generated by Django 4.2.4 on 2023-08-06 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('category', models.CharField(db_index=True, max_length=50)),
                ('high', models.FloatField(db_index=True, null=True)),
                ('low', models.FloatField(db_index=True, null=True)),
                ('average', models.FloatField(db_index=True, null=True)),
                ('date', models.DateField(db_index=True)),
            ],
        ),
    ]
