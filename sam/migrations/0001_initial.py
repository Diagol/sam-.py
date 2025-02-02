# Generated by Django 2.2.3 on 2019-07-04 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arranchar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Militares Arranchados',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=15, verbose_name='Categoria')),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Companhia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companhia', models.CharField(max_length=15, verbose_name='Companhia')),
            ],
            options={
                'verbose_name_plural': 'Companhia',
            },
        ),
        migrations.CreateModel(
            name='Dias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias_semana', models.CharField(max_length=15, verbose_name='Dia da Semana')),
            ],
            options={
                'verbose_name_plural': 'Dias da Semana',
            },
        ),
        migrations.CreateModel(
            name='Graduacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graduacao', models.CharField(max_length=15, verbose_name='Graduação')),
            ],
            options={
                'verbose_name_plural': 'Graduações',
            },
        ),
        migrations.CreateModel(
            name='OutrosArranchados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baixados', models.IntegerField(verbose_name='Militares Baixados')),
                ('servico', models.IntegerField(verbose_name='Militares de Serviço')),
                ('outro_batalhao', models.IntegerField(verbose_name='Militares de Outro Batalhão')),
            ],
            options={
                'verbose_name_plural': 'Outros Arranchados',
            },
        ),
        migrations.CreateModel(
            name='TotalArranchados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data')),
                ('arranchar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sam.Arranchar')),
                ('outros_arranchados', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sam.OutrosArranchados')),
            ],
            options={
                'verbose_name_plural': 'Total de Arranchados',
            },
        ),
        migrations.CreateModel(
            name='Cardapio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(verbose_name='Data')),
                ('cafe', models.CharField(max_length=300, verbose_name='Café')),
                ('almoco', models.CharField(max_length=300, verbose_name='Almoço')),
                ('janta', models.CharField(max_length=300, verbose_name='Jantar')),
                ('dia_semana', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sam.Dias')),
            ],
            options={
                'verbose_name_plural': 'Cardápio',
            },
        ),
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome de Guerra')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sam.Categoria')),
                ('companhia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sam.Companhia')),
                ('graduacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sam.Graduacoes')),
            ],
            options={
                'verbose_name_plural': 'Militares Cadastrados',
            },
        ),
        migrations.AddField(
            model_name='arranchar',
            name='dia_semana',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sam.Dias'),
        ),
        migrations.AddField(
            model_name='arranchar',
            name='militar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sam.Cadastro'),
        ),
    ]
