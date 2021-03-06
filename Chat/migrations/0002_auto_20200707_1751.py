# Generated by Django 3.0.8 on 2020-07-07 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='名前')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='メールアドレス')),
                ('comment', models.TextField(blank=True, max_length=1000, null=True, verbose_name='コメント')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.DeleteModel(
            name='TestUser',
        ),
    ]
