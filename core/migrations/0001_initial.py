# Generated by Django 2.1.7 on 2019-02-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=128)),
                ('url_length', models.PositiveIntegerField(blank=True, null=True)),
                ('job_id', models.CharField(blank=True, max_length=128, null=True)),
                ('result', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
    ]
