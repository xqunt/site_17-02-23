# Generated by Django 4.1.5 on 2023-02-06 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_postagem_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
