# Generated by Django 2.2.24 on 2021-09-05 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210905_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200, verbose_name='название статьи')),
                ('article_text', models.TextField(verbose_name='текст статьи')),
                ('pub_date', models.DateField(verbose_name='дата публикации')),
            ],
        ),
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=200, verbose_name='имя автора')),
                ('comment_text', models.CharField(max_length=200, verbose_name='текст комментария')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Article')),
            ],
        ),
    ]
