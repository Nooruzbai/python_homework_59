# Generated by Django 4.0.1 on 2022-02-21 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': [('can_see_user_list', 'Can see user list')], 'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
    ]