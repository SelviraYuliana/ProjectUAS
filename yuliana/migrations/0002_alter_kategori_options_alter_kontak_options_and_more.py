# Generated by Django 4.2.7 on 2023-11-29 16:20

import ckeditor.fields
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('yuliana', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategori',
            options={'verbose_name_plural': 'Data Kategori'},
        ),
        migrations.AlterModelOptions(
            name='kontak',
            options={'verbose_name_plural': 'Data kontak'},
        ),
        migrations.AlterModelOptions(
            name='produk',
            options={'verbose_name_plural': 'Data Produk'},
        ),
        migrations.AlterModelOptions(
            name='profil',
            options={'verbose_name_plural': 'Data Profil'},
        ),
        migrations.AlterModelOptions(
            name='slide',
            options={'verbose_name_plural': 'Data Slide'},
        ),
        migrations.AlterModelOptions(
            name='statis',
            options={'verbose_name_plural': 'Data Statis'},
        ),
        migrations.AddField(
            model_name='produk',
            name='aktif',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='kategori',
            name='banner_satu',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, scale=None, size=[575, 200], upload_to='gambar/banner', verbose_name='Gambar (575 x 200 pixel)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='diskon',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Diskon %'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='keterangan',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produk',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='keterangan',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
