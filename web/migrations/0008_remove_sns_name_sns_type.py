# Generated by Django 5.0.4 on 2024-04-28 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_sns_site'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sns',
            name='name',
        ),
        migrations.AddField(
            model_name='sns',
            name='type',
            field=models.CharField(choices=[('IG', 'INSTAGRAM')], default='IG', max_length=10, verbose_name='SNS名'),
            preserve_default=False,
        ),
    ]
