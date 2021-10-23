# Generated by Django 3.2.7 on 2021-09-05 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_stock_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('ticker', models.CharField(max_length=4)),
                ('sign', models.CharField(max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.currency'),
        ),
    ]
