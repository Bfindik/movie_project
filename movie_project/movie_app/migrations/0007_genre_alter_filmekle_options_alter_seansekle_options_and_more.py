# Generated by Django 4.2.1 on 2023-05-17 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_salonekle_alter_filmekle_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='filmekle',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='seansekle',
            options={'ordering': ['tarih']},
        ),
        migrations.AddField(
            model_name='filmekle',
            name='imdb_score',
            field=models.FloatField(default=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seansekle',
            name='altyazi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='seansekle',
            name='dublaj',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='salonekle',
            name='salon_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sinemaekle',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Bilet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bilet_tipi', models.CharField(choices=[('tam', 'Tam Bilet'), ('ogrenci', 'Öğrenci Bilet')], default='tam', max_length=10)),
                ('fiyat', models.DecimalField(decimal_places=2, max_digits=8)),
                ('adet', models.IntegerField()),
                ('seans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='biletler', to='movie_app.filmekle')),
            ],
        ),
        migrations.AddField(
            model_name='filmekle',
            name='genres',
            field=models.ManyToManyField(related_name='filmler', to='movie_app.genre'),
        ),
    ]
