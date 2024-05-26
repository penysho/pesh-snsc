# Generated by Django 5.0.4 on 2024-05-26 05:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_alter_snscuser_options_alter_site_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snsuseraccount',
            options={'verbose_name': 'SNSユーザーアカウントマスタ', 'verbose_name_plural': 'SNSユーザーアカウントマスタ'},
        ),
        migrations.AddField(
            model_name='postmedia',
            name='list_order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='一覧表示する際の優先度'),
        ),
        migrations.AlterField(
            model_name='postmedia',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_media', to='web.post'),
        ),
    ]
