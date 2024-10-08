# Generated by Django 5.0.4 on 2024-05-29 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_postmedia_uq_post_media_list_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('PRE', '未承認'), ('APR', '承認'), ('REJ', '却下'), ('DEL', '削除'), ('PND', '保留'), ('PUB', '公開'), ('UNP', '非公開'), ('ARC', 'アーカイブ')], default='PRE', max_length=10, verbose_name='投稿ステータス'),
        ),
    ]
