# Generated by Django 2.2 on 2021-09-29 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserImageCaptionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('filename', models.CharField(max_length=100)),
                ('results', models.CharField(max_length=1000)),
                ('file', models.FileField(upload_to='files/')),
                ('cdate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'usertestcaptions',
            },
        ),
    ]