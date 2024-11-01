# Generated by Django 2.1.5 on 2023-04-13 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ips', '0001_initial'),
        ('afiliacion', '0001_initial'),
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('financiacion', models.CharField(max_length=50)),
                ('afiliados', models.ManyToManyField(through='afiliacion.Afiliacion', to='pacientes.Paciente')),
                ('ipss', models.ManyToManyField(to='ips.Ips')),
            ],
        ),
    ]
