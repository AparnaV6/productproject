# Generated by Django 4.1.7 on 2023-04-02 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="img",
            field=models.ImageField(default="ddffdfs", upload_to="gallery"),
            preserve_default=False,
        ),
    ]
