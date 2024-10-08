# Generated by Django 5.0.4 on 2024-07-31 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0028_alter_postmedia_list_order_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='postmedia',
            name='uq_post_media_list_order',
        ),
        migrations.AddConstraint(
            model_name='postmedia',
            constraint=models.UniqueConstraint(fields=('post', 'list_order'), name='uq_post_media_post_list_order'),
        ),
    ]
