# Generated by Django 2.1 on 2018-08-27 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20180827_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
