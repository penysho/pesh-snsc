# Generated by Django 5.0.4 on 2024-04-28 04:36

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='投稿ユーザーネーム'),
        ),
        migrations.CreateModel(
            name='PostMedia',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='投稿メディア識別子')),
                ('type', models.CharField(max_length=20, verbose_name='投稿メディアタイプ')),
                ('sns_url', models.URLField(blank=True, max_length=1000, null=True, verbose_name='SNS側でホストされたURL')),
                ('hosted_list_url', models.FileField(blank=True, null=True, upload_to='list/', verbose_name='アプリケーションでホストされた一覧ページ用URL')),
                ('hosted_detail_url', models.FileField(upload_to='detail/', verbose_name='アプリケーションでホストされた詳細ページ用URL')),
                ('is_active', models.BooleanField(default=False, verbose_name='使用フラグ')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新日')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.post')),
            ],
            options={
                'verbose_name': '投稿メディアマスタ',
                'verbose_name_plural': '投稿メディアマスタ',
                'db_table': 'post_media',
            },
        ),
    ]