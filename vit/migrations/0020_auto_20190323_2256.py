# Generated by Django 2.1.7 on 2019-03-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vit', '0019_auto_20190323_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='title',
            field=models.CharField(default='abc', max_length=30),
        ),
        migrations.AlterUniqueTogether(
            name='material',
            unique_together={('fid', 'cid', 'mat')},
        ),
    ]
