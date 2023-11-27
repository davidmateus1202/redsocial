# Generated by Django 4.2.5 on 2023-11-03 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0002_alter_producto_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(blank=True, max_length=250)),
                ('ahora_agregado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='cartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarjetas.cart')),
                ('producto', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='store.producto')),
            ],
        ),
    ]
