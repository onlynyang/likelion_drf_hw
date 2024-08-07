# Generated by Django 5.0.3 on 2024-07-09 00:58

import django.db.models.deletion
import music.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_singer_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singer',
            name='image',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=music.models.image_upload_path)),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='music.singer')),
            ],
        ),
    ]
