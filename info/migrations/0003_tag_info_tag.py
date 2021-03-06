# Generated by Django 4.0.3 on 2022-04-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_alter_info_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='info',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='info.tag'),
        ),
    ]
