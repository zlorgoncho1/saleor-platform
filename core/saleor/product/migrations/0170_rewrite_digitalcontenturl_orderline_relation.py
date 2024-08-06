# Generated by Django 3.2.12 on 2022-04-13 07:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0143_update_orderline_pk"),
        ("product", "0169_alter_digitalcontenturl_line"),
    ]

    operations = [
        migrations.AlterField(
            model_name="digitalcontenturl",
            name="order_line_token",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="order.orderline",
            ),
        ),
        migrations.RemoveField(
            model_name="digitalcontenturl",
            name="line",
        ),
        migrations.RenameField(
            model_name="digitalcontenturl",
            old_name="order_line_token",
            new_name="line",
        ),
        migrations.AlterField(
            model_name="digitalcontenturl",
            name="line",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="digital_content_url",
                to="order.orderline",
            ),
        ),
    ]
