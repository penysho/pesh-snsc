# Generated by Django 5.0.4 on 2024-06-08 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0026_postproduct_postproductrelationship_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postproduct',
            options={'verbose_name': '投稿関連商品マスタ', 'verbose_name_plural': '投稿関連商品マスタ'},
        ),
        migrations.AlterField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='使用フラグ'),
        ),
        migrations.AlterField(
            model_name='postmedia',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='使用フラグ'),
        ),
        migrations.AlterField(
            model_name='postmedia',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_medias', to='web.post'),
        ),
        migrations.AlterField(
            model_name='postproduct',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='使用フラグ'),
        ),
        migrations.AlterField(
            model_name='postproduct',
            name='posts',
            field=models.ManyToManyField(related_name='post_products', through='web.PostProductRelationship', to='web.post'),
        ),
        migrations.AlterField(
            model_name='postproductrelationship',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='使用フラグ'),
        ),
        migrations.AlterField(
            model_name='site',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='使用フラグ'),
        ),
        migrations.AlterField(
            model_name='siteownership',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='使用フラグ'),
        ),
        migrations.AlterField(
            model_name='sns',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='使用フラグ'),
        ),
        migrations.AlterField(
            model_name='snsapiaccount',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='使用フラグ'),
        ),
        migrations.AlterField(
            model_name='snsuseraccount',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='使用フラグ'),
        ),
    ]