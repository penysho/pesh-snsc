# Generated by Django 5.0.4 on 2024-04-29 04:00

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_remove_sns_api_id_sns_account_id_sns_biography_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sns',
            options={'verbose_name': 'SNSサイト管理用マスタ', 'verbose_name_plural': 'SNSサイト管理用マスタ'},
        ),
        migrations.RemoveField(
            model_name='sns',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='sns',
            name='followers_count',
        ),
        migrations.RemoveField(
            model_name='sns',
            name='follows_count',
        ),
        migrations.RemoveField(
            model_name='sns',
            name='name',
        ),
        migrations.RemoveField(
            model_name='sns',
            name='post_count',
        ),
        migrations.RemoveField(
            model_name='sns',
            name='profile_picture_url',
        ),
        migrations.RemoveField(
            model_name='sns',
            name='username',
        ),
        migrations.RemoveField(
            model_name='sns',
            name='website',
        ),
        migrations.CreateModel(
            name='SnsUserAccount',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='SNSユーザーアカウント識別子')),
                ('username', models.CharField(blank=True, max_length=50, null=True, verbose_name='SNSユーザーネーム')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='SNSユーザー名(日本語対応)')),
                ('biography', models.TextField(blank=True, null=True, verbose_name='SNSユーザー説明文')),
                ('follows_count', models.IntegerField(blank=True, null=True, verbose_name='SNSユーザーフォロー数')),
                ('followers_count', models.IntegerField(blank=True, null=True, verbose_name='SNSユーザーフォロワー数')),
                ('post_count', models.IntegerField(blank=True, null=True, verbose_name='SNSユーザー投稿数')),
                ('profile_picture_url', models.URLField(blank=True, max_length=500, null=True, verbose_name='SNSユーザープロフィール画像URL')),
                ('website', models.URLField(blank=True, max_length=500, null=True, verbose_name='SNSユーザーウェブサイト')),
                ('is_active', models.BooleanField(default=False, verbose_name='使用フラグ')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新日')),
                ('sns', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.sns')),
            ],
            options={
                'verbose_name': 'SNSユーザーアカウントマスタ',
                'verbose_name_plural': 'SNSユーザーアカウントマスタタ',
                'db_table': 'sns_user_account',
            },
        ),
    ]
