# Generated by Django 4.2.5 on 2023-11-18 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_alter_producto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilventas',
            name='biografia_venta',
            field=models.TextField(blank=True, default='Editar biografia de vendendor', max_length=500),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firts_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('direccion', models.CharField(blank=True, max_length=255)),
                ('ciudad', models.CharField(blank=True, max_length=255)),
                ('departamento', models.CharField(blank=True, max_length=255)),
                ('pais', models.CharField(blank=True, max_length=255)),
                ('comentrio', models.TextField(blank=True, max_length=1000)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.producto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
