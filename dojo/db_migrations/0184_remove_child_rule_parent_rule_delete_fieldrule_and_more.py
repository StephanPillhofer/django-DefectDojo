# Generated by Django 4.1.7 on 2023-03-27 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0183_system_settings_enable_notify_sla_exponential_backoff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child_rule',
            name='parent_rule',
        ),
        migrations.DeleteModel(
            name='FieldRule',
        ),
        migrations.RemoveField(
            model_name='rule',
            name='child_rules',
        ),
        migrations.RemoveField(
            model_name='rule',
            name='parent_rule',
        ),
        migrations.RemoveField(
            model_name='system_settings',
            name='column_widths',
        ),
        migrations.RemoveField(
            model_name='system_settings',
            name='drive_folder_ID',
        ),
        migrations.RemoveField(
            model_name='system_settings',
            name='email_address',
        ),
        migrations.RemoveField(
            model_name='system_settings',
            name='enable_google_sheets',
        ),
        migrations.RemoveField(
            model_name='system_settings',
            name='enable_rules_framework',
        ),
        migrations.DeleteModel(
            name='Child_Rule',
        ),
        migrations.DeleteModel(
            name='Rule',
        ),
    ]