# Generated by Django 4.1.5 on 2023-02-15 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_sitecomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitecomment',
            old_name='post',
            new_name='site',
        ),
    ]
