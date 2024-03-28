# Generated by Django 4.2.7 on 2024-03-27 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indicateur', '0003_remove_client_id_csp_csp_id_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csp',
            name='id_client',
        ),
        migrations.AddField(
            model_name='client',
            name='id_csp',
            field=models.ForeignKey(default='6', on_delete=django.db.models.deletion.DO_NOTHING, related_name='csps', to='indicateur.csp'),
        ),
    ]