# Generated by Django 4.1.6 on 2023-03-25 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_blog_owner_alter_post_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blogs.blog'),
        ),
    ]
