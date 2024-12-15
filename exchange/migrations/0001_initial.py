# Generated by Django 3.1.12 on 2024-12-15 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConversionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_currency', models.CharField(max_length=3)),
                ('target_currency', models.CharField(max_length=3)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=30)),
                ('converted_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rate', models.DecimalField(decimal_places=6, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]