# Generated by Django 5.0.4 on 2024-05-03 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_article_managers_alter_author_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_date',
            field=models.DateField(auto_now=True),
        ),
    ]