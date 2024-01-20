# Generated by Django 4.2.7 on 2024-01-17 03:59

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('yuliana', '0003_rename_no_whatsup_kontak_no_whatsapp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategori',
            name='banner_dua',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, scale=None, size=[575, 200], upload_to='gambar/banner', verbose_name='Gambar (575 x 200 pixel)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, scale=None, size=[270, 250], upload_to='gambar/banner', verbose_name='Gambar (270 x 250 pixel)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar_dua',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, scale=None, size=[270, 250], upload_to='gambar/banner', verbose_name='Gambar (270 x 250 pixel)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar_empat',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, scale=None, size=[270, 250], upload_to='gambar/banner', verbose_name='Gambar (270 x 250 pixel)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar_lima',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, scale=None, size=[270, 250], upload_to='gambar/banner', verbose_name='Gambar (270 x 250 pixel)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar_satu',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, scale=None, size=[270, 250], upload_to='gambar/banner', verbose_name='Gambar (270 x 250 pixel)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar_tiga',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, scale=None, size=[270, 250], upload_to='gambar/banner', verbose_name='Gambar (270 x 250 pixel)'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='gambar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, scale=None, size=[1900, 1200], upload_to='gambar/banner', verbose_name='Gambar (1920 x 1200 pixel)'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='gambar_slide',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, scale=None, size=[475, 880], upload_to='gambar/banner', verbose_name='Gambar (475 x 880 pixel)'),
        ),
    ]
