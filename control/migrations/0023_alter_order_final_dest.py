# Generated by Django 4.2.13 on 2024-06-05 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0022_order_final_dest_alter_order_cash_registry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='final_dest',
            field=models.CharField(choices=[('J', 'Jemlenýär'), ('Mary', 'Mary'), ('Aşgabat', 'Aşgabat'), ('Lebap', 'Lebap'), ('Daşoguz', 'Daşoguz'), ('Balkan', 'Balkan')], max_length=50, verbose_name='Barmaly ýeri'),
        ),
    ]