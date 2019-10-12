# Generated by Django 2.2.6 on 2019-10-12 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=200)),
                ('isadmin', models.CharField(max_length=1)),
            ],
        ),
    ]