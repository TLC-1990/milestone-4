import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_product_sold"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image_2",
            field=cloudinary.models.CloudinaryField(
                blank=True, max_length=255, null=True, verbose_name="image_2"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="image_3",
            field=cloudinary.models.CloudinaryField(
                blank=True, max_length=255, null=True, verbose_name="image_3"
            ),
        ),
    ]
