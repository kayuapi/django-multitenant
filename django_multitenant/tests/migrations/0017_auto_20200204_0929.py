# Generated by Django 2.2.9 on 2020-02-04 09:29

from django.db import migrations
import django.db.models.deletion
import django_multitenant.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0016_auto_20191025_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='parent',
            field=django_multitenant.fields.TenantForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='tests.Task'),
        ),
    ]
